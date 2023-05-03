from django.urls import path
from .views import usuario_index

urlpatterns = [
    path('', usuario_index, name='usuario')
]
