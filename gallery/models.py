from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length=30)
  
  def __str__(self):
    return self.name
  
class Category(models.Model):
  name = models.CharField(max_length=30)
  
  def __str__(self):
    return self.name
  
class Image(models.Model):
  name = models.CharField(max_length=30)
  description = models.TextField()
  picture = models.ImageField(upload_to='images/',default='image')
  date = models.DateTimeField(auto_now_add=True)
  location = models.ForeignKey(Location,on_delete=models.CASCADE, default='location')
  category = models.ForeignKey(Category,on_delete=models.CASCADE, default='')
  
  def __str__(self):
    return self.name
  
  class Meta:
    ordering =['name']
  
  
