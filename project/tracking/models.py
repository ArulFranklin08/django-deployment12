from django.db import models

# Create your models here.
class Tracking(models.Model):
    sno = models.IntegerField(null=True)
    order_id = models.IntegerField(null=True)
    phone_no = models.IntegerField(null=True)
    Tracking_details = models.CharField(max_length=100, null=True)
    Tracking_place = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Tracking_details
