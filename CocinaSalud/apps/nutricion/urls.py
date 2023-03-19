from django.urls import path
from .views import *

# recetas/
urlpatterns = [
    path('', NutricionIndex.as_view(), name='nutricion'),
    path('<int:nutricion_id>', ver_nutricion, name='ver_nutricion'),
]