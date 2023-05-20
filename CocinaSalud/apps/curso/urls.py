from django.urls import path
from .views import CursosListView, CursoDetailView

urlpatterns = [
    path('', CursosListView.as_view(), name='cursos'),
    path('<slug:slug>/', CursoDetailView.as_view(), name='curso_detalle'),
]
