from django.urls import path
from django.views.generic import TemplateView
from apps.sitio.views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('acerca_de/', TemplateView.as_view(template_name='acerca_de.html'), name='acerca_de'),
    path('signup/', signup, name='signup'),
    path('accounts/login/', signin, name='signin'),
    path('sign_out/', sign_out, name='signout'),
    path('500', server_error, name='server_error'),
    path('404', page_not_found_error, name='page_not_found_error'),
]

handler500 = server_error
handler404 = page_not_found_error
handler403 = permission_denied_error