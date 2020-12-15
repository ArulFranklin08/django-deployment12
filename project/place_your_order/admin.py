from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class Place_your_orderAdmin(ImportExportModelAdmin):
    list_display = ['sno','Name','Company_name','Mobile']
    list_filter = ['Name']
    pass


admin.site.register(Place_your_order, Place_your_orderAdmin)
