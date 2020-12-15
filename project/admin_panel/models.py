from django.db import models
from datetime import  datetime, date
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

#from mptt.fields import TreeForeignKey
#from mptt.models import MPTTModel
# Create your models here.
class Customer(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active',),
        ('InActive', 'InActive',),
    )
    sno = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    order_id = models.IntegerField(null=True)
    cus_id = models.IntegerField(null=True)
    status =  models.CharField(max_length=100, null=True, choices=STATUS_CHOICES,)
    phone = PhoneNumberField(null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = (
        ('Success', 'Success',),
        ('Pending', 'Pending',),
        ('Processing ', 'Processing',),
    )
    sno = models.IntegerField(null=True)
    order_id = models.IntegerField(null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    status =  models.CharField(max_length=100, null=True, choices=STATUS_CHOICES,)
    item = models.CharField(max_length=100, null=True)
    shipping_address = models.CharField(max_length=100, null=True)
    billing_address = models.CharField(max_length=100, null=True)
    payment = models.CharField(max_length=100, null=True)
    total_amount = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    phone = PhoneNumberField(null=True)
    email = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name

class Blog(models.Model):
    sno = models.IntegerField(null=True)
    blog_category =  models.CharField(max_length=100, null=True)
    blog_name =  models.CharField(max_length=100, null=True)
    blog_image = models.ImageField(null=True, blank=True)
    image_alt_tag = models.CharField(max_length=100, null=True)
    title =  models.CharField(max_length=100, null=True)
    title_url = models.CharField(max_length=100, null=True)
    video = models.FileField(blank=True,upload_to='videos/')
    video_url = models.CharField(max_length=100, null=True)
    video_alt_tag = models.CharField(max_length=100, null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keywords = models.CharField(max_length=100, null=True)
    meta_description = models.TextField(null=True)

    def __str__(self):
        return self.blog_category

class Awarenes(models.Model):
    sno = models.IntegerField(null=True)
    title =  models.CharField(max_length=100, null=True)
    title_url = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    image_alt_tag = models.CharField(max_length=100, null=True)
    image_url = models.CharField(max_length=100, null=True)
    video = models.FileField(blank=True,upload_to='videos/')
    video_url = models.CharField(max_length=100, null=True)
    video_alt_tag = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    sno = models.IntegerField(null=True)
    User_name = models.CharField(max_length=100, null=True)
    phone = PhoneNumberField(null=True)
    email = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)
    description = models.TextField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    #timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.User_name

class Social_media(models.Model):
    sno = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100, null=True)
    video = models.FileField(blank=True,upload_to='videos/')
    video_url = models.CharField(max_length=100, null=True)
    video_alt_tag = models.CharField(max_length=100, null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keywords = models.CharField(max_length=100, null=True)
    meta_description = models.TextField(null=True)

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    sno = models.IntegerField(null=True)
    email =  models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.email

class Offers_code(models.Model):
    sno = models.IntegerField(null=True)
    offers_name = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    image_alt_tag = models.CharField(max_length=100, null=True)
    promo_code = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.offers_name

class Article(models.Model):
    sno = models.IntegerField(null=True)
    title = models.CharField(max_length=100, null=True)
    title_url = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    image_alt_tag = models.CharField(max_length=100, null=True)
    short_description = models.TextField(null=True)
    full_description = models.TextField(null=True)
    video = models.FileField(blank=True,upload_to='videos/')
    video_url = models.CharField(max_length=100, null=True)
    video_alt_tag = models.CharField(max_length=100, null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keywords = models.CharField(max_length=100, null=True)
    meta_description = models.TextField(null=True)

    def __str__(self):
        return self.title

class Article_category(models.Model):
    sno = models.IntegerField(null=True)
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    image_alt_tag = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name
