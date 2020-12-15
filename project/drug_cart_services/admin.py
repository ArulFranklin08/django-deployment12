from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class Physio_therapyAdmin(ImportExportModelAdmin):
    list_display = ['sno','doctor_name','gender','speciality','mobile_no','qualification']
    list_filter = ['doctor_name']
    pass

class Fitness_centreAdmin(ImportExportModelAdmin):
    list_display = ['sno','doctor_name','gender','speciality','mobile_no','qualification']
    list_filter = ['doctor_name']
    pass

class Spa_saloonAdmin(ImportExportModelAdmin):
    list_display = ['sno','doctor_name','gender','speciality','mobile_no','qualification']
    list_filter = ['doctor_name']
    pass

class YogaAdmin(ImportExportModelAdmin):
    list_display = ['sno','doctor_name','gender','speciality','mobile_no','qualification']
    list_filter = ['doctor_name']
    pass

class Cupping_therapyAdmin(ImportExportModelAdmin):
    list_display = ['sno','doctor_name','gender','speciality','mobile_no','qualification']
    list_filter = ['doctor_name']
    pass

class Stem_cell_theraphyAdmin(ImportExportModelAdmin):
    list_display = ['sno','doctor_name','gender','speciality','mobile_no','qualification']
    list_filter = ['doctor_name']
    pass


admin.site.register(Physio_therapy, Physio_therapyAdmin)
admin.site.register(Fitness_centre, Fitness_centreAdmin)
admin.site.register(Spa_saloon, Spa_saloonAdmin)
admin.site.register(Yoga, YogaAdmin)
admin.site.register(Cupping_therapy, Cupping_therapyAdmin)
admin.site.register(Stem_cell_theraphy, Stem_cell_theraphyAdmin)
