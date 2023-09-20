from django.urls import path
from .views import *

# recetas/
urlpatterns = [
    path('', SaludIndex.as_view(), name='salud'),
    path('<slug:salud_slug>', ver_salud, name='ver_salud'),
]