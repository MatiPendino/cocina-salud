from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Curso, CursoUsuario
from .utils import get_len_number_stars


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
        cursos_usuarios = CursoUsuario.objects.filter(curso=context['course'], state=True)
        # Receive all the course ratings, and convert them in a list
        # ratings = list(CursoUsuario.objects.filter(curso=context['course'], state=True).values_list('calificacion', flat=True))
        ratings = list(cursos_usuarios.values_list('calificacion', flat=True))
        # Obtain the length of each rating, and unpack the list in their varibles
        one_star, two_stars, three_stars, four_stars, five_stars = [get_len_number_stars(ratings, rating) for rating in range(1, 6)]
        context['one_star'] = one_star
        context['two_stars'] = two_stars
        context['three_stars'] = three_stars
        context['four_stars'] = four_stars
        context['five_stars'] = five_stars
        context['cursos_usuarios'] = cursos_usuarios
        quantity_ratings = sum([one_star, two_stars, three_stars, four_stars, five_stars])
        context['num_ratings'] = quantity_ratings
        if quantity_ratings > 0:
            context['one_star_p'] = one_star / quantity_ratings * 100
            context['two_stars_p'] = two_stars / quantity_ratings * 100
            context['three_stars_p'] = three_stars / quantity_ratings * 100
            context['four_stars_p'] = four_stars / quantity_ratings * 100
            context['five_stars_p'] = five_stars / quantity_ratings * 100
        else:
            context['one_star_p'] = 0
            context['two_stars_p'] = 0
            context['three_stars_p'] = 0
            context['four_stars_p'] = 0
            context['five_stars_p'] = 0
        return context