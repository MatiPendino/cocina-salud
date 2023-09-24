from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from apps.usuario_custom.models import Usuario
from apps.movimientos.models import MedioDePago, Movimiento
from apps.movimientos.utils import generate_unique_code
from .models import Curso, CursoUsuario, Leccion, LeccionUsuario
from .utils import get_slug_lesson_to_pass, get_percentage_rating \
    , get_lessons_for_section, update_last_seen_user_lesson, leave_review, complete_lesson \
    , has_user_course


class CursosListView(ListView):
    model = Curso
    queryset = Curso.objects.filter(state=True)
    context_object_name = 'courses'
    template_name = 'cursos/cursos.html'


class CursoDetailView(DetailView):
    model = Curso
    context_object_name = 'course'
    template_name ='cursos/curso_detalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cursos_usuarios = CursoUsuario.objects.filter(
            curso=context['course'], 
            state=True, 
            calificacion__gte=1
        )
        context['cursos_usuarios'] = cursos_usuarios

        ratings = list(cursos_usuarios.values_list('calificacion', flat=True))
        # Obtain how many qualifications each rating has
        one_star, two_stars, three_stars, four_stars, five_stars = [
            ratings.count(rating) for rating in range(1, 6)
        ]
        context['one_star'] = one_star
        context['two_stars'] = two_stars
        context['three_stars'] = three_stars
        context['four_stars'] = four_stars
        context['five_stars'] = five_stars

        num_ratings = sum([one_star, two_stars, three_stars, four_stars, five_stars])
        context['num_ratings'] = num_ratings

        context['one_star_p'] = get_percentage_rating(one_star, num_ratings)
        context['two_stars_p'] = get_percentage_rating(two_stars, num_ratings)
        context['three_stars_p'] = get_percentage_rating(three_stars, num_ratings)
        context['four_stars_p'] = get_percentage_rating(four_stars, num_ratings)
        context['five_stars_p'] = get_percentage_rating(five_stars, num_ratings)

        return context
    

class MisCursosListView(ListView):
    model = CursoUsuario
    context_object_name = 'user_courses'
    template_name = 'cursos/mis_cursos.html'

    def get_queryset(self):
        return CursoUsuario.objects.filter(curso__state=True, usuario__user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Make a list with the complete percentage of the user courses
        cursos_porc_completado = [
            user_course.curso.get_porcentaje_completado_curso(self.request.user) 
            for user_course in context['user_courses']
        ]

        # Override context['user_courses']. Zip the queryset (converted to list) user_courses
        # and the complete percentage list built above. Convert the outcome to dict
        context['user_courses'] = dict(zip(list(context['user_courses']), cursos_porc_completado))

        return context
    

class LeccionDetailView(DetailView):
    model = Leccion
    context_object_name = 'lesson'
    template_name = 'cursos/leccion.html'

    def get_queryset(self):
        return self.model.objects.filter(state=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curso = context['lesson'].seccion.curso

        curso_usuario = CursoUsuario.objects.filter(
            curso__id=curso.id,
            usuario__user=self.request.user
        ).first()
        context['curso_usuario'] = curso_usuario

        # Obtain all the course sections and the user lessons
        secciones = list(context['lesson'].get_secciones_curso())
        lecciones_usuario = LeccionUsuario.objects.filter(
            usuario__user=self.request.user, 
            leccion__seccion__curso=curso, 
            state=True
        ).order_by('leccion__orden')

        # Creation of a dictionary where the keys are the section names, and values
        # their corresponding list of user lessons
        secciones_lecciones_usuario = {
            seccion.nombre: get_lessons_for_section(lecciones_usuario, seccion)
            for seccion in secciones
        }
        context['secciones_lecciones_usuario'] = secciones_lecciones_usuario

        current_user_lesson = LeccionUsuario.objects.filter(
            usuario__user=self.request.user,
            leccion=context['lesson']
        ).first()
        context['leccion_usuario'] = current_user_lesson

        return context
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if not has_user_course(self):
            return redirect('curso_detalle', slug=self.object.seccion.curso.slug)
        
        update_last_seen_user_lesson(self)

        return response
    
    def post(self, request, *args, **kwargs):
        lesson_slug = request.POST['lesson']

        # In the HTML there are two forms, one for leaving a review and the other to mark
        # the lesson as completed.
        # In both forms, created a flag variable "action", to control which action we will apply
        if request.POST['action'] == 'review':
            leave_review(
                request.POST['curso_usuario'],
                request.POST['rating'],
                request.POST['comment']
            )
        elif request.POST['action'] == 'completed':
            complete_lesson(lesson_slug, request.user)

        return redirect('leccion_detalle', slug=lesson_slug)
    

def pass_lesson(request, current_lesson_slug, direction):
    lesson = Leccion.objects.filter(slug=current_lesson_slug).first()
    slug_lesson_to_pass = get_slug_lesson_to_pass(lesson, direction)
    
    return redirect('leccion_detalle', slug=slug_lesson_to_pass)


def last_seen_user_lesson(request, course_slug):
    user_lesson = LeccionUsuario.objects.filter(
        usuario__user=request.user,
        leccion__seccion__curso__slug=course_slug,
        ultima=True,
        state=True
    ).first()

    if user_lesson:
        return redirect('leccion_detalle', slug=user_lesson.leccion.slug)
    
    first_course_lesson = Leccion.objects.filter(
        seccion__curso__slug=course_slug,
        seccion__orden=1,
        orden=1,
        state=True
    ).first()
    return redirect('leccion_detalle', slug=first_course_lesson.slug)


def comprar_curso(request, course_slug):
    course = Curso.objects.filter(slug=course_slug, state=True).first()
    precio = str(course.precio).replace(',', '.')
    codigo_operacion = generate_unique_code()
    usuario = Usuario.objects.filter(user=request.user, state=True).first()
    paypal_mdp = MedioDePago.objects.filter(
        test=False, 
        tipo=MedioDePago.TIPO_PAYPAL, 
        state=True
    ).first()


    movimiento = Movimiento.objects.create(
        usuario=usuario,
        curso=course,
        medio_de_pago=paypal_mdp,
        importe=course.precio,
        descripcion=f'Compra curso {course.nombre} por parte de {usuario.get_username()} a través de {paypal_mdp.nombre}',
        condicion=Movimiento.ESTADO_INICIADA,
        codigo_operacion=codigo_operacion
    )

    context = {
        'course': course,
        'paypal_mdp': paypal_mdp,
        'movimiento': movimiento,
        'precio': precio
    }

    return render(request, 'cursos/comprar_curso.html', context)
    
