from django.urls import path
from apps.sitio import views

urlpatterns = [
    path("", views.index, name="index"),
    path("acerca_de/", views.acerca_de, name="acerca_de")
]