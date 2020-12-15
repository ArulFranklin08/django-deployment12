from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
# Create your models here.
class Health_check(models.Model):
    sno = models.IntegerField(null=True)
    Tiltle = models.CharField(max_length=100, null=True)
    Sub_title = models.CharField(max_length=100, null=True)
    Test_count = models.IntegerField(null=True)
    Consultant = models.CharField(max_length=100, null=True)
    image_url = models.CharField(max_length=100, null=True)
    image_alt_tag = models.CharField(max_length=100, null=True)
    Packages = RichTextField(blank=True, null=True)
    discount = models.IntegerField(null=True)
    work_days = models.CharField(max_length=100, null=True)
    work_hours = models.CharField(max_length=100, null=True)
    landline_no = models.IntegerField(null=True)
    video = models.FileField(blank=True,upload_to='videos/')
    video_url = models.CharField(max_length=100, null=True)
    video_alt_tag = models.CharField(max_length=100, null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keywords = models.CharField(max_length=100, null=True)
    meta_description = models.TextField(null=True)
    total_price = models.IntegerField(null=True)

    def __str__(self):
        return self.Tiltle
