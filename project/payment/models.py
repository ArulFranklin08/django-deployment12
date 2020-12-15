from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Payment(models.Model):
    sno = models.IntegerField(null=True)
    cus_no = models.IntegerField(null=True)
    card_no = models.IntegerField(null=True)
    Subscription_type = models.CharField(max_length=100, null=True)
    cus_type = models.CharField(max_length=100, null=True)
    trans_id = models.IntegerField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    phone_number = PhoneNumberField(null=True)
    email = models.CharField(max_length=100)
    total_amount = models.IntegerField(null=True)
    Currency = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.email

class Payment_Order(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active',),
        ('InActive', 'InActive',),
    )
    sno = models.IntegerField(null=True)
    Name = models.CharField(max_length=100)
    cus_type = models.CharField(max_length=100, null=True)
    trans_id = models.IntegerField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=100)
    total_amount = models.IntegerField(null=True)
    Address = models.TextField(null=True)
    phone_number = PhoneNumberField(null=True)
    Status = models.CharField(max_length=100, null=True, choices=STATUS_CHOICES,)



    def __str__(self):
        return self.Name

class Payment_Detail(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active',),
        ('InActive', 'InActive',),
    )
    sno = models.IntegerField(null=True)
    Customer_name = models.CharField(max_length=100)
    order_id = models.IntegerField(null=True)
    trans_id = models.IntegerField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=100)
    total_amount = models.IntegerField(null=True)
    Status = models.CharField(max_length=100, null=True, choices=STATUS_CHOICES,)


    def __str__(self):
        return self.Customer_name
