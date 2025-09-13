from django.urls import path
from .views import *

# recetas/
urlpatterns = [
    path('', EscuelaCocinaIndex.as_view(), name='escuela_cocina'),
    path('<slug:escuela_slug>', ver_escuela_cocina, name='ver_escuela_cocina')
]