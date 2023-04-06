from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class SaludResources(resources.ModelResource):
    class Meta:
        model = Salud


class SaludAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo',]
    list_display = ('titulo', 'creation_date', 'state')
    resource_class = SaludResources


class ItemSaludResources(resources.ModelResource):
    class Meta:
        model = ItemSalud


class ItemSaludAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo', 'descripcion']
    list_display = ('titulo', 'numero_item', 'salud')
    resource_class = ItemSaludResources


admin.site.register(Salud, SaludAdmin)
admin.site.register(ItemSalud, ItemSaludAdmin)