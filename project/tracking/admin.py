from django.contrib import admin
from .models import *
# Register your models here.
class TrackingAdmin(admin.ModelAdmin):
    list_display = ['sno','order_id','phone_no','Tracking_details']
    list_filter = ['phone_no']

admin.site.register(Tracking,TrackingAdmin)
