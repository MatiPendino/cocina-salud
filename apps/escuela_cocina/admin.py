from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class PasoTecnicaInline(admin.StackedInline):
    model = PasoTecnica
    extra = 1

class EscuelaCocinaResources(resources.ModelResource):
    class Meta:
        model = EscuelaCocina


class EscuelaCocinaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('titulo',)
    list_display = ('titulo', 'creation_date', 'state')
    resource_class = EscuelaCocinaResources
    inlines = [PasoTecnicaInline]


class PasoTecnicaResources(resources.ModelResource):
    class Meta:
        model = PasoTecnica


class PasoTecnicaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo', 'descripcion']
    list_display = ('titulo', 'numero_paso', 'escuela_cocina')
    resource_class = PasoTecnicaResources


admin.site.register(EscuelaCocina, EscuelaCocinaAdmin)
admin.site.register(PasoTecnica, PasoTecnicaAdmin)
