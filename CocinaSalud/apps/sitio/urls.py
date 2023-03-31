from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.sitio.views import *

urlpatterns = [
    path("", index, name="index"),
    path("acerca_de", acerca_de, name="acerca_de"),
    path("signup", signup, name="signup"),
    path("accounts/login/", signin, name="signin"),
    path("sign_out", sign_out, name="signout")
]