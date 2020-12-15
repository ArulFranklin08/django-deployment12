from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class Info_graphicAdmin(ImportExportModelAdmin):
    list_display = ['sno','title','title_url','image']
    list_filter = ['title']
    pass






admin.site.register(Info_graphic, Info_graphicAdmin)
