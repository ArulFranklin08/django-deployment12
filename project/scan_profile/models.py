from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
# Create your models here.
class Scan_entry(models.Model):
    SCAN_CHOICES = (
        ('Xray', 'Xray',),
        ('Ultra Sound', 'Ultra Sound',),
        ('CT', 'CT',),
        ('PET', 'PET',),
        ('MRI', 'PET',),
        ('EUS', 'EUS',),
        ('Bne Densitometry(DEXA)', 'Bne Densitometry(DEXA)',),
        ('Fluoroscopy', 'Fluoroscopy',),
        ('Mammography', 'Mammography',),
    )
    sno = models.IntegerField(null=True)
    scan_center_name = models.CharField(max_length=100, null=True)
    company_name = models.CharField(max_length=100, null=True)
    business_start = models.CharField(max_length=100, null=True)
    no_of_employee = models.IntegerField(null=True)
    work_days = models.IntegerField(null=True)
    mobile_no = PhoneNumberField(null=True)
    landline_no = models.IntegerField(null=True)
    lab_email = models.CharField(max_length=100, null=True)
    lab_url = models.CharField(max_length=100, null=True)
    lab_logo = models.ImageField(blank=True,upload_to='images/')
    lab_image = models.ImageField(blank=True,upload_to='images/')
    image = models.ImageField(blank=True,upload_to='images/')
    image_alt_tag = models.CharField(max_length=100, null=True)
    #lab_logo_url = models.CharField(max_length=100, null=True)
    #lab_image_url = models.CharField(max_length=100, null=True)
    #lab_alt_image = models.CharField(max_length=100, null=True)
    #lab_logo_alt_tag = models.CharField(max_length=20, null=True)
    #video_upload = models.FileField(blank=True,upload_to='videos/')
    #video_url = models.CharField(max_length=20, null=True)
    #video_alt_tag = models.CharField(max_length=20, null=True)
    service_provider = models.CharField(max_length=100, null=True)
    street_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    pincode = models.IntegerField(null=True)
    scan_name =  models.CharField(max_length=100, choices=SCAN_CHOICES,)
    price = models.IntegerField(null=True)
    scan_test_list = models.TextField(null=True)
    google_location = models.CharField(max_length=100, null=True)
    about_lab_description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.scan_center_name

class Scan_package(models.Model):
    sno = models.IntegerField(null=True)
    scan_package_name = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True,upload_to='images/')

    def __str__(self):
        return self.scan_package_name

class Scan_booking(models.Model):
    GENDER_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',),
        ('Transgender', 'Transgender',),
    )

    sno = models.IntegerField(null=True)
    doctor_name = models.CharField(max_length=100, null=True)
    consulation = models.CharField(max_length=100, null=True)
    scan = models.CharField(max_length=100, null=True)
    profile_for = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,)
    email = models.CharField(max_length=20, null=True)
    mobile = PhoneNumberField(null=True)
    payment = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.doctor_name
