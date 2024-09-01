from django.db import models

class LeccionManager(models.Manager):
    def get_slug_leccion(self, leccion_actual, direccion):
        """
        Recibe la lección actual y la dirección (next o previous) y obtiene el slug de la 
        lección a redirigir
        """
        if direccion == 'next':
            # If there is a following lesson in the section, return its id. Otherwise,
            # pass to the next section.
            next_lesson = self.filter(
                seccion=leccion_actual.seccion,
                orden=leccion_actual.orden + 1
            ).first()
            if next_lesson:
                return next_lesson.slug
            else:
                # If there is a following section in the course, return the id of its first
                # lesson. Otherwise, we reached the final of the course
                next_lesson = self.filter(
                    seccion__orden=leccion_actual.seccion.orden + 1,
                    seccion__curso=leccion_actual.seccion.curso,
                    orden=1
                ).first()
                if next_lesson:
                    return next_lesson.slug
                else:
                    return leccion_actual.slug

        elif direccion == 'previous':
            # If there is a previous lesson in the section, return its id. Otherwise,
            # come back to the previous section.
            previous_lesson = self.filter(
                seccion=leccion_actual.seccion,
                orden=leccion_actual.orden - 1
            ).first()
            if previous_lesson:
                return previous_lesson.slug
            else:
                # If there is a previous section in the course, return the id of its last
                # lesson. Otherwise, we reached the beginning of the course
                previous_lesson = self.filter(
                    seccion__orden=leccion_actual.seccion.orden - 1,
                    seccion__curso=leccion_actual.seccion.curso
                ).order_by('-orden').first()
                if previous_lesson:
                    return previous_lesson.slug
                else:
                    return leccion_actual.slug
                

class CursoUsuarioManager(models.Manager):
    def existe_curso_usuario(self, user, curso) -> bool:
        """Verifica si el user posee el curso"""
        if user.is_authenticated:
            curso_usuario = self.filter(usuario__user=user, curso=curso)
            return curso_usuario.exists()
        
        return False