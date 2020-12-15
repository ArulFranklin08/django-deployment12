from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
#from countrycode.models import Order

# Register your models here.
class Add_country_codeAdmin(ImportExportModelAdmin):
    list_display = ['sno','country_name','country_code','country_flag']
    list_filter = ['country_name']

class List_of_country_codeAdmin(ImportExportModelAdmin):
    list_display = ['sno','country_name','country_code','country_flag']
    list_filter = ['country_name']


admin.site.register(Add_country_code,Add_country_codeAdmin)
admin.site.register(List_of_country_code,List_of_country_codeAdmin)
