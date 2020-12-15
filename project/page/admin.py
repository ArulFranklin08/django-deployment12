from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.
class Error_pageAdmin(ImportExportModelAdmin):
    list_display = ['sno','Page_name','Page_url','create_date','update_date']
    list_filter = ['Page_name']
    pass

class Other_pageAdmin(ImportExportModelAdmin):
    list_display = ['sno','Page_name','Description','create_date','update_date']
    list_filter = ['Page_name']
    pass

class Total_pageAdmin(ImportExportModelAdmin):
    list_display = ['sno','Page_name','Page_url','create_date','update_date']
    list_filter = ['Page_name']
    pass

class Trending_pageAdmin(ImportExportModelAdmin):
    list_display = ['sno','view_count','activity','create_date','update_date']
    list_filter = ['activity']
    pass

admin.site.register(Error_page, Error_pageAdmin)
admin.site.register(Other_page, Other_pageAdmin)
admin.site.register(Total_page, Total_pageAdmin)
admin.site.register(Trending_page, Trending_pageAdmin)
