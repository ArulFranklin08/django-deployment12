from django.db import models

# Create your models here.
class Country(models.Model):
    sno = models.IntegerField(null=True)
    country_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.country_name

class State(models.Model):
    sno = models.IntegerField(null=True)
    state_name = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.state_name

class District(models.Model):
    sno = models.IntegerField(null=True)
    state_name = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    district_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.district_name

class Area(models.Model):
    sno = models.IntegerField(null=True)
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    state_name = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    district_name = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    area = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.area
