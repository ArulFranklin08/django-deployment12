from django.db import models
from datetime import  datetime, date
from django.utils import timezone
# Create your models here.
class Health_tracker(models.Model):
    sno = models.IntegerField(null=True)
    Enter_Triglycerides_in_mg_dl = models.IntegerField(null=True)
    Select_Date = models.DateField(null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
