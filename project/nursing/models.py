from django.db import models

# Create your models here.
class Home_nurse(models.Model):
    SERVICE_CHOICES = (
        ('Immediately', 'Immediately',),
        ('In the next 3 days', 'In the next 3 days',),
        ('In the next 7 days', 'In the next 7 days',),
        ('In the next 15 days', 'In the next 15 days',),
        ('After a month', 'After a month',),
    )
    TYPE_SERVICE_CHOICES = (
        ('Part Time', 'Part Time',),
        ('Full Time-Non-Live-in', 'In the next 3 days',),
        ('Full Time-Live-in', 'In the next 7 days',),
    )
    GENDER_SERVICE_CHOICES = (
        ('Any', 'Any',),
        ('Male', 'Male',),
        ('Female', 'Female',),
    )
    REQUIREMENT_CHOICES = (
        ('Post operative assistance', 'Post operative assistance',),
        ('Administration injuctions', 'Administration injuctions',),
        ('Monitoring vitals', 'Monitoring vitals',),
        ('Daily Assistance', 'Daily Assistance',),
        ('Mobility Assistance', 'Mobility Assistance',),
        ('Feeding and Making meals', 'Feeding and Making meals',),
        ('Others', 'Others',),
    )
    NEED_SERVICE_CHOICES = (
        ('Elder Parents', 'Elder Parents',),
        ('Grand Parents(Senior Citizens)', 'Grand Parents(Senior Citizens)',),
        ('Relatives', 'Relatives',),
        ('Friend', 'Friend',),
        ('Self', 'Self',),
    )

    sno = models.IntegerField(null=True)
    What_do_you_need_the_service = models.CharField(max_length=100, null=True, choices=SERVICE_CHOICES,)
    What_type_of_service_do_you_need = models.CharField(max_length=100, null=True, choices=TYPE_SERVICE_CHOICES,)
    Select_the_preferred_gender_of_the_homenurse = models.CharField(max_length=100, null=True, choices=GENDER_SERVICE_CHOICES,)
    what_are_the_requirement_for_the_service = models.CharField(max_length=100, null=True, choices=REQUIREMENT_CHOICES,)
    For_whom_do_you_need_service = models.CharField(max_length=100, null=True, choices=NEED_SERVICE_CHOICES ,)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.What_do_you_need_the_service
