from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
# Create your models here.
class Package(models.Model):
    sno = models.IntegerField(null=True)
    package_name = models.CharField(max_length=100, null=True)
    package_url = models.CharField(max_length=100, null=True)
    package_image = models.ImageField(blank=True,upload_to='images/')
    package_image_url = models.CharField(max_length=100, null=True)
    image_alt_tag = models.CharField(max_length=20, null=True)
    video_upload = models.FileField(blank=True,upload_to='videos/')
    video_url = models.CharField(max_length=20, null=True)
    video_alt_tag = models.CharField(max_length=20, null=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.package_name


class Lab_entry(models.Model):
    sno = models.IntegerField(null=True)
    lab_name = models.CharField(max_length=100, null=True)
    business_start = models.CharField(max_length=100, null=True)
    no_of_employee = models.IntegerField(null=True)
    work_days = models.IntegerField(null=True)
    mobile_no = PhoneNumberField(null=True)
    landline_no = models.IntegerField(null=True)
    lab_email = models.CharField(max_length=100, null=True)
    lab_url = models.CharField(max_length=100, null=True)
    lab_logo = models.ImageField(blank=True,upload_to='images/')
    lab_logo_url = models.CharField(max_length=100, null=True)
    lab_image = models.ImageField(blank=True,upload_to='images/')
    lab_image_url = models.CharField(max_length=100, null=True)
    lab_alt_image = models.CharField(max_length=100, null=True)
    lab_logo_alt_tag = models.CharField(max_length=20, null=True)
    video_upload = models.FileField(blank=True,upload_to='videos/')
    video_url = models.CharField(max_length=20, null=True)
    video_alt_tag = models.CharField(max_length=20, null=True)
    service_provider = models.CharField(max_length=100, null=True)
    street_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    pincode = models.IntegerField(null=True)
    package =  models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True)
    package_test_list = models.TextField(null=True)
    about_lab_description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.lab_name


class List_of_lab_booking(models.Model):
    sno = models.IntegerField(null=True)
    profile_for = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    package = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True,upload_to='images/')
    phone = PhoneNumberField(null=True)
    image_url = models.CharField(max_length=20, null=True)
    image_alt_tag = models.CharField(max_length=20, null=True)
    video_url = models.CharField(max_length=20, null=True)
    video_alt_tag = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
