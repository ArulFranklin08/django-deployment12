from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

class Post_Image(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post.title


class Main_slider(models.Model):
    sno = models.IntegerField(null=True)
    home_slider = models.ImageField(blank=True)
    image_alt_tag = models.CharField(max_length=100, null=True)
    image_url = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.image_alt_tag



class A_side_banner(models.Model):
    CATEGORY_CHOICES = (
        ('firstside', 'firstside',),
        ('secondside', 'secondside',),
    )
    sno = models.IntegerField(null=True)
    category_name = models.CharField(max_length=20, choices=CATEGORY_CHOICES,)
    banner_images = models.ImageField(blank=True,upload_to='images/')
    image_alt_tag = models.CharField(max_length=100, null=True)
    image_url = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.category_name

class Drug_carts_service(models.Model):
    sno = models.IntegerField(null=True)
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True,upload_to='images/')
    image_alt_tag = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.title

class Special_care(models.Model):
    sno = models.IntegerField(null=True)
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True,upload_to='images/')
    image_alt_tag = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.title

class Clinic(models.Model):
    sno = models.IntegerField(null=True)
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True,upload_to='images/')
    image_alt_tag = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.title

class Pick_opportunity(models.Model):
    sno = models.IntegerField(null=True)
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True,upload_to='images/')
    image_alt_tag = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.title
