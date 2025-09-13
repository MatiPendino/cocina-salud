from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def calificacion_estrella(calificacion):
    full_estrella = '<i class="bi bi-star-fill"></i>'
    half_estrella = '<i class="bi bi-star-half"></i>'
    empty_estrella = '<i class="bi bi-star"></i>'

    stars = ''
    if calificacion <= 1.2:
        stars = full_estrella + empty_estrella * 4
    elif 1.3 <= calificacion <= 1.7:
        stars = full_estrella + half_estrella + empty_estrella * 3
    elif 1.8 <= calificacion <= 2.2:
        stars = full_estrella * 2 + empty_estrella * 3
    elif 2.3 <= calificacion <= 2.7:
        stars = full_estrella * 2 + half_estrella + empty_estrella * 2
    elif 2.8 <= calificacion <= 3.2:
        stars = full_estrella * 3 + empty_estrella * 2
    elif 3.3 <= calificacion <= 3.7:
        stars = full_estrella * 3 + half_estrella + empty_estrella * 1
    elif 3.8 <= calificacion <= 4.2:
        stars = full_estrella * 4 + empty_estrella * 1
    elif 4.3 <= calificacion <= 4.7:
        stars = full_estrella * 4 + half_estrella
    elif calificacion >= 4.8:
        stars = full_estrella * 5
    else:
        stars = empty_estrella * 5

    return mark_safe(stars)


@register.simple_tag
def calificacion_estrella_usuario(calificacion):
    full_estrella = '<i class="bi bi-star-fill"></i>'
    empty_estrella = '<i class="bi bi-star"></i>'

    stars = ''
    if calificacion == 1:
        stars = full_estrella + empty_estrella * 4
    elif calificacion == 2:
        stars = full_estrella * 2 + empty_estrella * 3
    elif calificacion == 3:
        stars = full_estrella * 3 + empty_estrella * 2
    elif calificacion == 4:
        stars = full_estrella * 4 + empty_estrella * 1
    elif calificacion == 5:
        stars = full_estrella * 5
    else:
        stars = empty_estrella * 5

    return mark_safe(stars)