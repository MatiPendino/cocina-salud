from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Movimiento, MedioDePago


class MedioDePagoResources(resources.ModelResource):
    class Meta:
        model = MedioDePago

class MedioDePagoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('nombre', 'tipo', 'moneda_codigo')
    list_display = ('nombre', 'tipo', 'moneda_codigo')
    resource_class = MedioDePagoResources

admin.site.register(MedioDePago, MedioDePagoAdmin)


class MovimientoResources(resources.ModelResource):
    class Meta:
        model = Movimiento

class MovimientoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('usuario__user__username', 'descripcion')
    list_display = ('usuario', 'importe', 'descripcion')
    resource_class = MovimientoResources

admin.site.register(Movimiento, MovimientoAdmin)