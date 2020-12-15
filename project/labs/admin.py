from django.contrib import admin
from .models import *
from .models import Lab, Add_extra_field
from import_export.admin import ImportExportModelAdmin
# Register your models here.
'''class LabAdmin(ImportExportModelAdmin):
    list_display = ['sno','lab_name','lab_url','amount','lab_email','location','total_price']
    list_filter = ['lab_name']'''



class Add_extra_fieldAdmin(admin.StackedInline):
    model=Add_extra_field


@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    inlines = [Add_extra_fieldAdmin]

    class Meta:
        model = Lab

@admin.register(Add_extra_field)
class Add_extra_fieldAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Lab, LabAdmin)
