from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CursosListView, CursoDetailView, MisCursosListView, LeccionDetailView \
    , pass_lesson, last_seen_user_lesson, comprar_curso

urlpatterns = [
    path('', CursosListView.as_view(), name='cursos'),
    path('mis_cursos/', login_required(MisCursosListView.as_view()), name='mis_cursos'),
    path('<slug:slug>/', CursoDetailView.as_view(), name='curso_detalle'),
    path('leccion/<slug:slug>/', login_required(LeccionDetailView.as_view()), name='leccion_detalle'),
    path('pass_lesson/<slug:current_lesson_slug>/<str:direction>/', pass_lesson, name='pass_lesson'),
    path('last_seen_lesson/<slug:course_slug>/', login_required(last_seen_user_lesson), name='last_seen_user_lesson'),
    path('comprar_curso/<slug:course_slug>/', login_required(comprar_curso), name='comprar_curso')
]
