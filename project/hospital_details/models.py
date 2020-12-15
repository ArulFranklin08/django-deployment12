from django.db import models
#from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
# Create your models here.
class Hospital_type(models.Model):
    sno = models.IntegerField(null=True)
    hospital_type = models.CharField(max_length=100)
    hospital_url = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True,upload_to='images/')
    image_url = models.CharField(max_length=100, null=True)
    image_alt_tag = models.CharField(max_length=20, null=True)
    doctor_image_url = models.CharField(max_length=100, null=True)
    description = RichTextField(blank=True, null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_description = models.CharField(max_length=100, null=True)
    meta_keyword = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.hospital_type



class Hospital_entry(models.Model):
    sno = models.IntegerField(null=True)
    hospital_type = models.CharField(max_length=100)
    image = models.ImageField(blank=True,upload_to='images/')
    image_url = models.CharField(max_length=100, null=True)
    image_alt_tag = models.CharField(max_length=20, null=True)
    doctor_image_url = models.CharField(max_length=100, null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_description = models.CharField(max_length=100, null=True)
    meta_keyword = models.CharField(max_length=100, null=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.hospital_type

class Hospital_booking(models.Model):
    sno = models.IntegerField(null=True)
    hospital_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = PhoneNumberField(null=True)
    payment =  models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.hospital_name
