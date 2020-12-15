from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
# Create your models here.
class Error_page(models.Model):
    STATUS_CHOICES = (
        ('Solved', 'Solved',),
        ('Unsolved', 'Unsolved',),
    )
    sno = models.IntegerField(null=True)
    Page_name = models.CharField(max_length=100, null=True)
    Page_url = models.CharField(max_length=100, null=True)
    Page_id = models.IntegerField(null=True)
    Error_type = models.CharField(max_length=100, null=True)
    View_count = models.IntegerField(null=True)
    Status = models.CharField(max_length=100, null=True, choices=STATUS_CHOICES,)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Page_name

class Other_page(models.Model):
    sno = models.IntegerField(null=True)
    Page_name = models.CharField(max_length=100, null=True)
    Page_url = models.CharField(max_length=100, null=True)
    Description = RichTextField(blank=True, null=True)
    Meta_title = models.CharField(max_length=100, null=True)
    Meta_description = models.TextField(max_length=100, null=True)
    Meta_tag = models.CharField(max_length=100, null=True)
    Page_maintained_by = models.CharField(max_length=100, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    #activity = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Page_name

class Total_page(models.Model):
    sno = models.IntegerField(null=True)
    Page_name = models.CharField(max_length=100, null=True)
    Page_url = models.CharField(max_length=100, null=True)
    Error_Page = models.CharField(max_length=100, null=True)
    Today_page = models.IntegerField(null=True)
    view_count = models.IntegerField(null=True)
    Bounce_rate = models.IntegerField(null=True)
    Page_maintained_by = models.CharField(max_length=100, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    #activity = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Page_name

class Trending_page(models.Model):
    sno = models.IntegerField(null=True)
    Page_id = models.IntegerField(null=True)
    Page_name = models.CharField(max_length=100, null=True)
    Page_url = models.CharField(max_length=100, null=True)
    phone_number = PhoneNumberField(null=True)
    view_count = models.IntegerField(null=True)
    Total_page = models.IntegerField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    activity = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.activity
