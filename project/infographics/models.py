from django.db import models

# Create your models here.
class Info_graphic(models.Model):
    sno = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    title_url = models.CharField(max_length=100)
    image = models.ImageField(blank=True,upload_to='images/')
    img_alt_tag = models.CharField(max_length=100)
    video_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title
