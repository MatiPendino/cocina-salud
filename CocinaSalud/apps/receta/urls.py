from django.urls import path
from .views import *

# recetas/
urlpatterns = [
    path('', RecetasIndex.as_view(), name='recetas'),
    path('<slug:receta_slug>/', ver_receta, name='ver_receta')
]