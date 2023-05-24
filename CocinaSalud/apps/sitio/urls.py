from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.sitio.views import *

urlpatterns = [
    path('', index, name='index'),
    path('acerca_de/', acerca_de, name='acerca_de'),
    path('signup/', signup, name='signup'),
    path('accounts/login/', signin, name='signin'),
    path('sign_out/', sign_out, name='signout'),
    path('500', server_error, name='server_error'),
    path('404', page_not_found_error, name='page_not_found_error'),
    path('403', permission_denied_error, name='permission_denied_error')
]

handler500 = server_error
handler404 = page_not_found_error
handler403 = permission_denied_error