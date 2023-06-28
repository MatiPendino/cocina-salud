from django.urls import path
from .views import compra_finalizada, compra_no_finalizada, ipn

urlpatterns = [
    path('compra_finalizada/<slug:course_slug>/<str:codigo_operacion>/', 
        compra_finalizada, name='compra_finalizada'),
    path('compra_no_finalizada/<slug:course_slug>/<str:codigo_operacion>/', 
        compra_no_finalizada, name='compra_no_finalizada'),
    path('ipn/<str:codigo_operacion>/', ipn, name='ipn'),
]
