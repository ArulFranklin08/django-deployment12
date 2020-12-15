from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
# Create your models here.
class Lab(models.Model):
    sno = models.IntegerField(null=True)
    lab_name = models.CharField(max_length=100, null=True)
    lab_url = models.CharField(max_length=100, null=True)
    subway_team = RichTextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    amount = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    work_days = models.CharField(max_length=100, null=True)
    package_image_url = models.CharField(max_length=100, null=True)
    landline_no = models.IntegerField(null=True)
    lab_email = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    total_price = models.IntegerField(null=True)

    def __str__(self):
        return self.lab_name


class Add_extra_field(models.Model):
    field = models.ForeignKey(Lab, default=None, on_delete=models.CASCADE)
    extra_field = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.field.lab_name
