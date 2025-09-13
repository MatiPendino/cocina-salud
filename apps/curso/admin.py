from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Curso, Seccion, Leccion, CursoUsuario, LeccionUsuario


class SeccionInline(admin.StackedInline):
    model = Seccion
    extra = 1

class CursoResources(resources.ModelResource):
    class Meta:
        model = Curso

class CursoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'calificacion', 'num_alumnos')
    search_fields = ('nombre', 'descripcion_breve')
    resource_class = CursoResources
    inlines = [SeccionInline]



class LeccionInline(admin.StackedInline):
    model = Leccion
    extra = 1

class SeccionResources(resources.ModelResource):
    class Meta:
        model = Seccion

class SeccionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('nombre', 'curso__nombre')
    list_display = ('nombre', 'curso', 'orden')
    resource_class = SeccionResources
    inlines = [LeccionInline]


class LeccionResources(resources.ModelResource):
    class Meta:
        model = Leccion

class LeccionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'seccion')
    search_fields = ('nombre', 'seccion__nombre', 'seccion__curso__nombre')
    resource_class = LeccionResources


class CursoUsuarioResources(resources.ModelResource):
    class Meta:
        model = CursoUsuario

class CursoUsuarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('curso__nombre', 'usuario__user__username')
    list_display = ('curso', 'usuario', 'calificacion')
    resource_class = CursoUsuarioResources


class LeccionUsuarioResources(resources.ModelResource):
    class Meta:
        model = LeccionUsuario

class LeccionUsuarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('leccion__nombre', 'usuario__user__username')
    list_display = ('leccion', 'usuario', 'completada')
    resource_class = LeccionUsuarioResources


admin.site.register(Curso, CursoAdmin)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Leccion, LeccionAdmin)
admin.site.register(CursoUsuario, CursoUsuarioAdmin)
admin.site.register(LeccionUsuario, LeccionUsuarioAdmin)
