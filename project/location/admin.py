from django.contrib import admin
from .models import *

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ['sno','country_name']
    list_filter = ['country_name']

class StateAdmin(admin.ModelAdmin):
    list_display = ['sno','state_name']
    list_filter = ['state_name']

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['sno','state_name', 'district_name']
    list_filter = ['district_name']

class AreaAdmin(admin.ModelAdmin):
    list_display = ['sno','country_name','state_name', 'district_name', 'area']
    list_filter = ['area']

admin.site.register(State, StateAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Country, CountryAdmin)
#admin.site.register(Product,ProductAdmin)
