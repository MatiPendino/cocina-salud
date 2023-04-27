from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Movimiento


class MovimientoResources(resources.ModelResource):
    class Meta:
        model = Movimiento


class MovimientoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('usuario__user__username', 'descripcion')
    list_display = ('usuario', 'importe', 'descripcion')
    resource_class = MovimientoResources


admin.site.register(Movimiento, MovimientoAdmin)