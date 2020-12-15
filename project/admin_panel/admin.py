from django.contrib import admin
from .models import *
from datetime import  datetime, date
from django.utils import timezone
from import_export.admin import ImportExportModelAdmin
#from adminpanel.models import (Order, Customer, Blog, Awarenes,Feedback, Socialmedia, Newsletter, Offerscode, Article)
#from mptt.admin import DraggableMPTTAdmin

# Register your models here.

class OrderAdmin(ImportExportModelAdmin):
    list_display = ['sno','order_id','datetime','status','item','shipping_address','payment','name','phone','total_amount']
    list_filter = ['status']

class CustomerAdmin(ImportExportModelAdmin):
    list_display = ['sno','order_id','name','phone']
    list_filter = ['name']
    pass

class BlogAdmin(ImportExportModelAdmin):
    list_display = ['sno','blog_category','blog_name','title']
    list_filter = ['blog_category']

class AwarenesAdmin(ImportExportModelAdmin):
    list_display = ['sno','title','datetime']
    list_filter = ['title']

class FeedbackAdmin(ImportExportModelAdmin):
    list_display = ['sno','User_name','phone','email','date']
    list_filter = ['User_name']

class Social_mediaAdmin(ImportExportModelAdmin):
    list_display = ['sno','name','link']
    list_filter = ['name']

class NewsletterAdmin(ImportExportModelAdmin):
    list_display = ['sno','email']
    list_filter = ['email']

class Offers_codeAdmin(ImportExportModelAdmin):
    list_display = ['sno','offers_name','image','promo_code']
    list_filter = ['offers_name']

class ArticleAdmin(ImportExportModelAdmin):
    list_display = ['sno','title','image']
    list_filter = ['title']

class Article_categoryAdmin(ImportExportModelAdmin):
    list_display = ['sno','image','name']
    list_filter = ['name']


#admin.site.register(Category,CategoryAdmin2)
#admin.site.register(Product)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Awarenes, AwarenesAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Social_media, Social_mediaAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Offers_code, Offers_codeAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Article_category, Article_categoryAdmin)
