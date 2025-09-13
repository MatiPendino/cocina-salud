from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class NutricionResources(resources.ModelResource):
    class Meta:
        model = Nutricion


class NutricionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('titulo',)
    list_display = ('titulo', 'creation_date', 'state')
    resource_class = NutricionResources

admin.site.register(Nutricion, NutricionAdmin)
