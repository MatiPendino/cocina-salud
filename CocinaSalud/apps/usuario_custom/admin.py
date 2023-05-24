from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Usuario


class UsuarioResources(resources.ModelResource):
    class Meta:
        model = Usuario


class UsuarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('user__username',)
    list_display = ('user',)
    resource_class = UsuarioResources


admin.site.register(Usuario, UsuarioAdmin)