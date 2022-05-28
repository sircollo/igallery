from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Image(models.Model):
  name = models.CharField(max_length=30)
  description = models.TextField()
  picture = models.ImageField(upload_to='images',default='image')
  date = models.DateTimeField(auto_now_add=True)