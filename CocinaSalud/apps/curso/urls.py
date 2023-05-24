from django.urls import path
from .views import CursosListView, CursoDetailView, MisCursosListView, LeccionDetailView

urlpatterns = [
    path('', CursosListView.as_view(), name='cursos'),
    path('mis_cursos/', MisCursosListView.as_view(), name='mis_cursos'),
    path('<slug:slug>/', CursoDetailView.as_view(), name='curso_detalle'),
    path('leccion/<int:pk>/', LeccionDetailView.as_view(), name='leccion_detalle'),
]
