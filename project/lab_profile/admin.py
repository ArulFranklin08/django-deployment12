from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class PackageAdmin(ImportExportModelAdmin):
    list_display = ['sno','package_name','package_image']
    list_filter = ['package_name']


class Lab_entryAdmin(ImportExportModelAdmin):
    list_display = ['sno','lab_name','package','no_of_employee','work_days']
    list_filter = ['lab_name']

class List_of_lab_bookingAdmin(ImportExportModelAdmin):
    list_display = ['sno','profile_for','name','package','phone']
    list_filter = ['name']



admin.site.register(Package, PackageAdmin)
admin.site.register(Lab_entry, Lab_entryAdmin)
admin.site.register(List_of_lab_booking, List_of_lab_bookingAdmin)
