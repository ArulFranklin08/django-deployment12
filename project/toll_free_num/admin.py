from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.
class Toll_Free_NumAdmin(ImportExportModelAdmin):
    list_display = ['sno','Name','Phone_no']
    list_filter = ['Name']
    pass

admin.site.register(Toll_Free_Num, Toll_Free_NumAdmin)
