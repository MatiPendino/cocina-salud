from django.urls import path
from .views import *

# recetas/
urlpatterns = [
    path('', NutricionIndex.as_view(), name='nutricion'),
    path('<slug:nutricion_slug>', ver_nutricion, name='ver_nutricion'),
]