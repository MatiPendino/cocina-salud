from django.contrib import admin
from django.urls import path, include, re_path
from apps.sitio import urls as sitio_urls
from apps.receta import urls as receta_urls
from apps.nutricion import urls as nutricion_urls
from apps.escuela_cocina import urls as escuela_urls
from apps.salud import urls as salud_urls
from apps.usuario_custom import urls as usuario_urls
from apps.curso import urls as curso_urls
from apps.movimientos import urls as movimientos_urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.static import serve
from CocinaSalud.settings.base import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(sitio_urls)),
    path('recetas/', include(receta_urls)),
    path('escuela_cocina/', include(escuela_urls)),
    path('salud/', include(salud_urls)),
    path('nutricion/', include(nutricion_urls)),
    path('curso/', include(curso_urls)),
    path('user/', include(usuario_urls)),
    path('movimientos/', include(movimientos_urls))
] 

urlpatterns += staticfiles_urlpatterns()
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]

