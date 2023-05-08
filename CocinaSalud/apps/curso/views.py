from django.shortcuts import render
from django.views.generic import ListView
from .models import Curso


class CursosListView(ListView):
    model = Curso
    queryset = Curso.objects.filter(state=True)
    context_object_name = 'courses'
    template_name = 'cursos/cursos.html'
