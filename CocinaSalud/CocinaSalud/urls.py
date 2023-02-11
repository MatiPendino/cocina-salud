"""CocinaSalud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.sitio import urls as sitio_urls
from apps.receta import urls as receta_urls
from apps.nutricion import urls as nutricion_urls
from apps.escuela_cocina import urls as escuela_urls
from apps.salud import urls as salud_urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(sitio_urls)),
    path("recetas/", include(receta_urls)),
    path("escuela_cocina/", include(escuela_urls)),
    path("salud/", include(salud_urls)),
    path("nutricion/", include(nutricion_urls))
]

urlpatterns += staticfiles_urlpatterns()

