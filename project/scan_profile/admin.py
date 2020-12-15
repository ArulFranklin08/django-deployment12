from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class Scan_entryAdmin(ImportExportModelAdmin):
    list_display = ['sno','scan_center_name','no_of_employee','mobile_no']
    list_filter = ['scan_center_name']
    pass

class Scan_packageAdmin(ImportExportModelAdmin):
    list_display = ['sno','scan_package_name','image']
    list_filter = ['scan_package_name']
    pass

class Scan_bookingAdmin(ImportExportModelAdmin):
    list_display = ['sno','doctor_name','scan','payment']
    list_filter = ['doctor_name']
    pass



admin.site.register(Scan_entry, Scan_entryAdmin)
admin.site.register(Scan_package, Scan_packageAdmin)
admin.site.register(Scan_booking, Scan_bookingAdmin)
