from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class Hospital_typeAdmin(ImportExportModelAdmin):
    list_display = ['sno','hospital_type']
    list_filter = ['hospital_type']

class Hospital_entryAdmin(ImportExportModelAdmin):
    list_display = ['sno','hospital_type']
    list_filter = ['hospital_type']

class Hospital_bookingAdmin(ImportExportModelAdmin):
    list_display = ['sno','hospital_name','doctor_name','patient_name','email','phone_number','payment']
    list_filter = ['doctor_name']


admin.site.register(Hospital_type, Hospital_typeAdmin)
admin.site.register(Hospital_entry, Hospital_entryAdmin)
admin.site.register(Hospital_booking, Hospital_bookingAdmin)
