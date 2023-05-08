from django.urls import path
from .views import CursosListView

urlpatterns = [
    path('', CursosListView.as_view(), name='cursos'),
]
