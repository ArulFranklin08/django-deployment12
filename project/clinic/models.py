from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
# Create your models here.
class Add_clinic(models.Model):
    GENDER_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',),
        ('Transgender', 'Transgender',),
    )
    CATEGORY_CHOICES = (
        ('Drug Addiction Clinic', 'Drug Addiction Clinic',),
        ('STD Clinic', 'STD Clinic',),
        ('Nutrition Clinic', 'Nutrition Clinic',),
        ('Baby Clinic', 'Baby Clinic',),
        ('Urgent & Emergency Care Clinic', 'Urgent & Emergency Care Clinic',),
        ('Male Fertlity Clinic', 'Male Fertlity Clinic',),
        ('Female Fertlity Clinic', 'Female Fertlity Clinic',),
        ('Baby Adoption', 'Baby Adoption',),
        ('Poly Clinic', 'Poly Clinic',),
    )
    sno = models.IntegerField(null=True)
    Category_type = models.CharField(max_length=100,null=True, choices=CATEGORY_CHOICES,)
    Clinic_name = models.CharField(max_length=100, null=True)
    Clinic_url = models.CharField(max_length=100, null=True)
    Clinic_image = models.ImageField(blank=True,upload_to='images/')
    Contact_person = models.CharField(max_length=100, null=True)
    About_clinic = models.TextField( null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES,)
    image_alt_tag = models.CharField(max_length=20, null=True)
    video_upload = models.FileField(blank=True,upload_to='videos/')
    video_url = models.CharField(max_length=20, null=True)
    video_alt_tag = models.CharField(max_length=20, null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keywords = models.CharField(max_length=100, null=True)
    meta_description = models.TextField(null=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.Clinic_name

class Clinic_booking(models.Model):
    sno = models.IntegerField(null=True)
    Category = models.CharField(max_length=100, null=True)
    clinic_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    About_clinic = models.CharField(max_length=100, null=True)
    phone_number = PhoneNumberField(null=True)
    city = models.CharField(max_length=100)

    #payment =  models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.Category
