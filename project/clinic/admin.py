from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class Add_clinicAdmin(ImportExportModelAdmin):
    list_display = ['sno','Category_type','Clinic_name','gender']
    list_filter = ['Category_type']
    pass

class Clinic_bookingAdmin(ImportExportModelAdmin):
    list_display = ['sno','Category','clinic_name','phone_number']
    list_filter = ['Category']
    pass


admin.site.register(Add_clinic, Add_clinicAdmin)
admin.site.register(Clinic_booking, Clinic_bookingAdmin)
