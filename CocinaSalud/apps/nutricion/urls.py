from django.urls import path
from .views import *

# recetas/
urlpatterns = [
    path('', NutricionIndex.as_view(), name='nutricion_index'),
    path('<int:nutricion_id>', ver_nutricion, name='ver_nutricion'),
]