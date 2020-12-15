from django.contrib import admin
from .models import *
# Register your models here.

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['sno','customer_name','email','plan_subscription']
    list_filter = ['customer_name']

class Subscription_paymentAdmin(admin.ModelAdmin):
    list_display = ['sno','Customer_name','order_id','trans_id','create_date','email','total_amount','update_date',]
    list_filter = ['create_date']


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Subscription_payment, Subscription_paymentAdmin)
