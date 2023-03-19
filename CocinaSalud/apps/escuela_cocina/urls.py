from django.urls import path
from .views import *

# recetas/
urlpatterns = [
    path('', EscuelaCocinaIndex.as_view(), name='escuela_cocina'),
    path('<int:escuela_id>', ver_escuela_cocina, name='ver_escuela_cocina')
]