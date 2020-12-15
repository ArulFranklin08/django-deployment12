from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Toll_Free_Num(models.Model):
    sno = models.IntegerField(null=True)
    Name = models.CharField(max_length=100, null=True)
    Phone_no = PhoneNumberField(null=True)
    Comment = models.CharField(max_length=100, null=True)
    Count = models.IntegerField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    #activity = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Name
