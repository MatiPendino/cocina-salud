from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class RecetaResources(resources.ModelResource):
    class Meta:
        model = Receta

class RecetaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('titulo',)
    list_display = ('titulo', 'creation_date', 'state')
    resource_class = RecetaResources


class PasoRecetaResources(resources.ModelResource):
    class Meta:
        model = PasoReceta


class PasoRecetaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('titulo',)
    list_display = ('titulo', 'numero_paso', 'receta')
    resource_class = PasoRecetaResources


admin.site.register(Receta, RecetaAdmin)
admin.site.register(PasoReceta, PasoRecetaAdmin)
