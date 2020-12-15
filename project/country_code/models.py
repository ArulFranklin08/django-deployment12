from django.db import models

# Create your models here.
class Add_country_code(models.Model):
    sno = models.IntegerField(null=True)
    country_name = models.CharField(max_length=100, null=True)
    country_code = models.IntegerField(null=True)
    country_flag = models.ImageField(blank=True,upload_to='images/')
    image_alt_tag = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.country_name

class List_of_country_code(models.Model):
    sno = models.IntegerField(null=True)
    country_name = models.CharField(max_length=100, null=True)
    country_code = models.IntegerField(null=True)
    country_flag = models.ImageField(blank=True,upload_to='images/')
    image_alt_tag = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.country_name
