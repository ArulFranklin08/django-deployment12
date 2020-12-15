from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Physio_therapy(models.Model):
    GENDER_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',),
        ('Transgender', 'Transgender',),
    )
    STATUS_CHOICES = (
        ('Available', 'Available',),
        ('Unavailable', 'Unavailable',),
    )
    sno = models.IntegerField(null=True)
    doctor_name = models.CharField(max_length=100, null=True)
    mobile_no = PhoneNumberField(null=True)
    email = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES,)
    qualification = models.CharField(max_length=20, null=True)
    speciality = models.CharField(max_length=20, null=True)
    doctor_image = models.ImageField(blank=True,upload_to='images/')
    doctor_image_url = models.CharField(max_length=20, null=True)
    doctor_alt_image = models.CharField(max_length=20, null=True)
    clinic_name = models.CharField(max_length=20, null=True)
    clinic_image = models.ImageField(blank=True,upload_to='images/')
    clinic_image_url = models.CharField(max_length=20, null=True)
    clinic_alt_image = models.CharField(max_length=20, null=True)
    street_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    pincode = models.IntegerField(null=True)
    working_days = models.CharField(max_length=20, null=True)
    morning_timing = models.CharField(max_length=20, null=True)
    evening_timing = models.CharField(max_length=20, null=True)
    google_location = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,)
    notes = models.TextField(null=True)

    def __str__(self):
        return self.doctor_name

class Fitness_centre(models.Model):
    GENDER_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',),
        ('Transgender', 'Transgender',),
    )
    STATUS_CHOICES = (
        ('Available', 'Available',),
        ('Unavailable', 'Unavailable',),
    )
    sno = models.IntegerField(null=True)
    doctor_name = models.CharField(max_length=100, null=True)
    mobile_no = PhoneNumberField(null=True)
    email = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES,)
    qualification = models.CharField(max_length=20, null=True)
    speciality = models.CharField(max_length=20, null=True)
    doctor_image = models.ImageField(blank=True,upload_to='images/')
    doctor_image_url = models.CharField(max_length=20, null=True)
    doctor_alt_image = models.CharField(max_length=20, null=True)
    clinic_name = models.CharField(max_length=20, null=True)
    clinic_image = models.ImageField(blank=True,upload_to='images/')
    clinic_image_url = models.CharField(max_length=20, null=True)
    clinic_alt_image = models.CharField(max_length=20, null=True)
    street_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    pincode = models.IntegerField(null=True)
    working_days = models.CharField(max_length=20, null=True)
    morning_timing = models.CharField(max_length=20, null=True)
    evening_timing = models.CharField(max_length=20, null=True)
    google_location = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,)
    notes = models.TextField(null=True)

    def __str__(self):
        return self.doctor_name


class Spa_saloon(models.Model):
    GENDER_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',),
        ('Transgender', 'Transgender',),
    )
    STATUS_CHOICES = (
        ('Available', 'Available',),
        ('Unavailable', 'Unavailable',),
    )
    sno = models.IntegerField(null=True)
    doctor_name = models.CharField(max_length=100, null=True)
    mobile_no = PhoneNumberField(null=True)
    email = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES,)
    qualification = models.CharField(max_length=20, null=True)
    speciality = models.CharField(max_length=20, null=True)
    doctor_image = models.ImageField(blank=True,upload_to='images/')
    doctor_image_url = models.CharField(max_length=20, null=True)
    doctor_alt_image = models.CharField(max_length=20, null=True)
    clinic_name = models.CharField(max_length=20, null=True)
    clinic_image = models.ImageField(blank=True,upload_to='images/')
    clinic_image_url = models.CharField(max_length=20, null=True)
    clinic_alt_image = models.CharField(max_length=20, null=True)
    street_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    pincode = models.IntegerField(null=True)
    working_days = models.CharField(max_length=20, null=True)
    morning_timing = models.CharField(max_length=20, null=True)
    evening_timing = models.CharField(max_length=20, null=True)
    google_location = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,)
    notes = models.TextField(null=True)

    def __str__(self):
        return self.doctor_name

class Yoga(models.Model):
    GENDER_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',),
        ('Transgender', 'Transgender',),
    )
    STATUS_CHOICES = (
        ('Available', 'Available',),
        ('Unavailable', 'Unavailable',),
    )
    sno = models.IntegerField(null=True)
    doctor_name = models.CharField(max_length=100, null=True)
    mobile_no = PhoneNumberField(null=True)
    email = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES,)
    qualification = models.CharField(max_length=20, null=True)
    speciality = models.CharField(max_length=20, null=True)
    doctor_image = models.ImageField(blank=True,upload_to='images/')
    doctor_image_url = models.CharField(max_length=20, null=True)
    doctor_alt_image = models.CharField(max_length=20, null=True)
    clinic_name = models.CharField(max_length=20, null=True)
    clinic_image = models.ImageField(blank=True,upload_to='images/')
    clinic_image_url = models.CharField(max_length=20, null=True)
    clinic_alt_image = models.CharField(max_length=20, null=True)
    street_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    pincode = models.IntegerField(null=True)
    working_days = models.CharField(max_length=20, null=True)
    morning_timing = models.CharField(max_length=20, null=True)
    evening_timing = models.CharField(max_length=20, null=True)
    google_location = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,)
    notes = models.TextField(null=True)

    def __str__(self):
        return self.doctor_name
class Cupping_therapy(models.Model):
    GENDER_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',),
        ('Transgender', 'Transgender',),
    )
    STATUS_CHOICES = (
        ('Available', 'Available',),
        ('Unavailable', 'Unavailable',),
    )
    sno = models.IntegerField(null=True)
    doctor_name = models.CharField(max_length=100, null=True)
    mobile_no = PhoneNumberField(null=True)
    email = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES,)
    qualification = models.CharField(max_length=20, null=True)
    speciality = models.CharField(max_length=20, null=True)
    doctor_image = models.ImageField(blank=True,upload_to='images/')
    doctor_image_url = models.CharField(max_length=20, null=True)
    doctor_alt_image = models.CharField(max_length=20, null=True)
    clinic_name = models.CharField(max_length=20, null=True)
    clinic_image = models.ImageField(blank=True,upload_to='images/')
    clinic_image_url = models.CharField(max_length=20, null=True)
    clinic_alt_image = models.CharField(max_length=20, null=True)
    street_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    pincode = models.IntegerField(null=True)
    working_days = models.CharField(max_length=20, null=True)
    morning_timing = models.CharField(max_length=20, null=True)
    evening_timing = models.CharField(max_length=20, null=True)
    google_location = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,)
    notes = models.TextField(null=True)

    def __str__(self):
        return self.doctor_name

class Stem_cell_theraphy(models.Model):
    GENDER_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',),
        ('Transgender', 'Transgender',),
    )
    STATUS_CHOICES = (
        ('Available', 'Available',),
        ('Unavailable', 'Unavailable',),
    )
    sno = models.IntegerField(null=True)
    doctor_name = models.CharField(max_length=100, null=True)
    mobile_no = PhoneNumberField(null=True)
    email = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES,)
    qualification = models.CharField(max_length=20, null=True)
    speciality = models.CharField(max_length=20, null=True)
    doctor_image = models.ImageField(blank=True,upload_to='images/')
    doctor_image_url = models.CharField(max_length=20, null=True)
    doctor_alt_image = models.CharField(max_length=20, null=True)
    clinic_name = models.CharField(max_length=20, null=True)
    clinic_image = models.ImageField(blank=True,upload_to='images/')
    clinic_image_url = models.CharField(max_length=20, null=True)
    clinic_alt_image = models.CharField(max_length=20, null=True)
    street_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    pincode = models.IntegerField(null=True)
    working_days = models.CharField(max_length=20, null=True)
    morning_timing = models.CharField(max_length=20, null=True)
    evening_timing = models.CharField(max_length=20, null=True)
    google_location = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,)
    notes = models.TextField(null=True)

    def __str__(self):
        return self.doctor_name
