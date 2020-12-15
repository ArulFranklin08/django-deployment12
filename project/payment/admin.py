from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class PaymentAdmin(ImportExportModelAdmin):
    list_display = ['sno','cus_no','trans_id','create_date','email','total_amount','Currency','update_date']
    list_filter = ['create_date']
    pass

class Payment_OrderAdmin(ImportExportModelAdmin):
    list_display = ['sno','Name','cus_type','trans_id','create_date','email','total_amount','Status','update_date']
    list_filter = ['create_date']
    pass

class Payment_DetailAdmin(ImportExportModelAdmin):
    list_display = ['sno','Customer_name','order_id','trans_id','create_date','email','total_amount','Status','update_date']
    list_filter = ['create_date']
    pass

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Payment_Order, Payment_OrderAdmin)
admin.site.register(Payment_Detail, Payment_DetailAdmin)
