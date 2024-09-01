from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.conf import settings
from django.http import Http404
from apps.curso.selectors import get_leccion_usuario_actual, get_curso_usuario, get_cursos_usuarios_calificacion, get_leccion_usuario_last_seen, get_leccion_usuario, get_primera_leccion
from apps.movimientos.services import create_movimiento
from apps.usuario_custom.models import Usuario
from apps.movimientos.models import MedioDePago
from apps.movimientos.utils import generate_unique_code
from .models import Curso, CursoUsuario, Leccion, LeccionUsuario
from .utils import *
from .services import dejar_resenia, get_estrellas, get_secciones_lecciones_usuario, update_last_seen_leccion_usuario

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

        cursos_usuarios = get_cursos_usuarios_calificacion(curso=context['course'])
        context['cursos_usuarios'] = cursos_usuarios
        context['estrellas'] = get_estrellas(cursos_usuarios)

        return context
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        user = self.request.user
        course = self.object

        # Si el usuario ya compró el curso, se le redirige a la última lección vista,
        # caso contrario se retorna la response
        if CursoUsuario.objects.existe_curso_usuario(user, course):
            return redirect('last_seen_user_lesson', course_slug=self.object.slug)
        
        return response
    

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

        context['curso_usuario'] = get_curso_usuario(curso_id=curso.id, user=self.request.user)
        context['secciones_lecciones_usuario'] = get_secciones_lecciones_usuario(
            user=self.request.user,
            curso=curso
        )
        context['leccion_usuario'] = get_leccion_usuario_actual(
            user=self.request.user, 
            leccion=context['lesson']
        )

        return context
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        user = self.request.user 
        course = self.object.seccion.curso

        # Si el usuario no compró el curso, se le redirige al detalle del mismo,
        # caso contrario se actualiza la última lección vista por el usuario y
        # se retorna la response
        if not CursoUsuario.objects.existe_curso_usuario(user, course):
            return redirect('curso_detalle', slug=course.slug)
        
        update_last_seen_leccion_usuario(user=self.request.user, leccion=self.object)

        return response
    
    def post(self, request, *args, **kwargs):
        lesson_slug = request.POST['lesson']

        # In the HTML there are two forms, one for leaving a review and the other to mark
        # the lesson as completed.
        # In both forms, created a flag variable "action", to control which action we will apply
        if request.POST['action'] == 'review':
            dejar_resenia(
                request.POST['curso_usuario'],
                request.POST['rating'],
                request.POST['comment']
            )
        elif request.POST['action'] == 'completed':
            try:
                leccion_usuario = get_leccion_usuario(leccion_slug=lesson_slug, user=request.user)
            except LeccionUsuario.DoesNotExist:
                raise Http404('leccion_usuario no encontrado')
            leccion_usuario.complete_lesson()

        return redirect('leccion_detalle', slug=lesson_slug)
    

def pass_lesson(request, current_lesson_slug, direction):
    leccion = get_object_or_404(Leccion, slug=current_lesson_slug)
    proximo_slug = Leccion.objects.get_slug_leccion(leccion, direction)
    
    return redirect('leccion_detalle', slug=proximo_slug)


def last_seen_user_lesson(request, course_slug):
    # Si ya existe una última lección vista por el usuario, redireccionamos a esa
    # caso contrario, obtenemos la primer lección del curso y hacemos la redirección
    user_lesson = get_leccion_usuario_last_seen(user=request.user, curso_slug=course_slug)
    if user_lesson:
        return redirect('leccion_detalle', slug=user_lesson.leccion.slug)

    try:
        primera_leccion_curso = get_primera_leccion(curso_slug=course_slug) 
    except Leccion.DoesNotExist:
        raise Http404('Lección no encontrada')
    return redirect('leccion_detalle', slug=primera_leccion_curso.slug)


def comprar_curso(request, course_slug):
    curso = get_curso(course_slug)
    precio = get_precio_str(curso)
    codigo_operacion = generate_unique_code()
    usuario = get_object_or_404(Usuario, user=request.user, state=True)
    paypal_mdp = get_object_or_404(
        MedioDePago, 
        test=settings.DEBUG, 
        tipo=MedioDePago.TIPO_PAYPAL, 
        state=True
    )
    
    movimiento = create_movimiento(curso, usuario, paypal_mdp, codigo_operacion)
    context = {
        'course': curso if curso else None,
        'paypal_mdp': paypal_mdp,
        'movimiento': movimiento,
        'precio': precio
    } 

    return render(request, 'cursos/comprar_curso.html', context)
    
