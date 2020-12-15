from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class List_of_doctorAdmin(ImportExportModelAdmin):
    list_display = ['sno','doctor_name','gender','speciality','mobile_no','qualification']
    list_filter = ['doctor_name']

class Doctor_entryAdmin(ImportExportModelAdmin):
    list_display = ['sno','doctor_name','gender','speciality','mobile_no','qualification']
    list_filter = ['doctor_name']

class List_of_doctor_bookingAdmin(ImportExportModelAdmin):
    list_display = ['sno','doctor_name','consulation','patient_name','gender','profile_for','payment']
    list_filter = ['doctor_name']

admin.site.register(List_of_doctor, List_of_doctorAdmin)
admin.site.register(Doctor_entry, Doctor_entryAdmin)
admin.site.register(List_of_doctor_booking, List_of_doctor_bookingAdmin)
