from django.contrib import admin
from .models import *
from catlog.models import  Category,Product
from import_export.admin import ImportExportModelAdmin
#from mptt.admin import DraggableMPTTAdmin

# Register your models here.
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['sno','category_name','category_type']
    list_filter = ['category_name']

class Sub_categoryAdmin(ImportExportModelAdmin):
    list_display = ['sno','category_name','subcategory_name']
    list_filter = ['category_name']

class ProductAdmin(ImportExportModelAdmin):
    list_display = ['sno','category','sub_category','product_name','manufactuer','mrp']
    list_filter = ['product_name']

class BrandAdmin(ImportExportModelAdmin):
    list_display = ['sno','name','image','image_url']
    list_filter = ['name']
    pass


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Sub_category,Sub_categoryAdmin)
