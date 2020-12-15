from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class Home_nurseAdmin(ImportExportModelAdmin):
    list_display = ['sno','What_do_you_need_the_service','What_type_of_service_do_you_need',
                    'Select_the_preferred_gender_of_the_homenurse']
    list_filter = ['What_do_you_need_the_service']


admin.site.register(Home_nurse, Home_nurseAdmin)
