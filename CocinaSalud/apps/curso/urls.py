from django.urls import path
from .views import CursosListView, CursoDetailView, MisCursosListView, LeccionDetailView \
    , pass_lesson, last_seen_user_lesson

urlpatterns = [
    path('', CursosListView.as_view(), name='cursos'),
    path('mis_cursos/', MisCursosListView.as_view(), name='mis_cursos'),
    path('<slug:slug>/', CursoDetailView.as_view(), name='curso_detalle'),
    path('leccion/<int:pk>/', LeccionDetailView.as_view(), name='leccion_detalle'),
    path('pass_lesson/<int:current_lesson_id>/<str:direction>/', pass_lesson, name='pass_lesson'),
    path('last_seen_lesson/<slug:course_slug>/', last_seen_user_lesson, name='last_seen_user_lesson'),
]
