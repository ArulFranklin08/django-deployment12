from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Subscription(models.Model):
    STATUS_CHOICES = (
        ('Gold', 'Gold',),
        ('Platinum', 'Platinum',),
        ('Bronze', 'Bronze',),
    )
    sno = models.IntegerField(null=True)
    customer_name = models.CharField(max_length=30, null=True)
    #category_id = models.IntegerField(null=True)
    email = models.CharField(max_length=100, null=True)
    phone = PhoneNumberField(null=True)
    plan_subscription = models.CharField(max_length=100, null=True, choices=STATUS_CHOICES,)
    payment = models.CharField(max_length=100, null=True)
    Address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.customer_name

class Subscription_payment(models.Model):
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
    models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.Customer_name
