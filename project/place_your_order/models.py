from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Place_your_order(models.Model):
    sno = models.IntegerField(null=True)
    Name = models.CharField(max_length=100, null=True)
    Company_name = models.CharField(max_length=100)
    Mobile = PhoneNumberField(null=True)
    Email = models.CharField(max_length=100, null=True)
    Address = models.CharField(max_length=100, null=True)
    State = models.CharField(max_length=100, null=True)
    City = models.CharField(max_length=100, null=True)
    Landmark = models.CharField(max_length=100, null=True)
    Pincode = models.IntegerField(null=True)
    Sanitizer = models.IntegerField(null=True)
    Hand_gloves = models.IntegerField(null=True)
    Mask = models.IntegerField(null=True)
    Thermometer = models.IntegerField(null=True)
    PPE_kit = models.IntegerField(null=True)

    def __str__(self):
        return self.Name
