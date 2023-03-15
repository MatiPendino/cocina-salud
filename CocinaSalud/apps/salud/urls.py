from django.urls import path
from .views import *

# recetas/
urlpatterns = [
    path('', SaludIndex.as_view(), name='salud_index'),
    path('<int:salud_id>', ver_salud, name='ver_salud'),
]