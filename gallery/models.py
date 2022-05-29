from distutils.command.upload import upload
from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length=30)
  
  def __str__(self):
    return self.name
  
  def save_location(self):
    self.save()
    
 
  @classmethod 
  def update_location(cls, id, value):
    cls.objects.filter(id=id).update(name=value)
    
  def delete_location(self):
    self.delete()
    
  
class Category(models.Model):
  name = models.CharField(max_length=30)
  
  def __str__(self):
    return self.name
  
  def save_category(self):
    self.save()
    
  @classmethod 
  def update_category(cls, id, value):
    cls.objects.filter(id=id).update(name=value)
    
  def delete_category(self):
    self.delete()
  
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
    
  def save_image(self):
    self.save()
  
  @classmethod
  def update_image(cls,id,value):
    cls.objects.filter(id=id).update(picture=value)
  

  def delete_image(self):
    self.delete()
  
  @classmethod
  def get_image_by_id(cls, id):
    image = cls.objects.filter(id=id).all()
    return image
  
  @classmethod
  def search_by_category(cls, search_term):
      images = cls.objects.filter(category__name__icontains=search_term)
      return images
  
  @classmethod
  def filter_by_location(cls, location):
    image_location = Image.objects.filter(location__name=location).all()
    return image_location
    
class Video(models.Model):
  video = EmbedVideoField()
  
  def __str__(self):
    return self.video
  
