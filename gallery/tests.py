from django.test import TestCase
from .models import *
# Create your tests here.

#location testcase
class LocationTestCase(TestCase):
  #setup method
  def setUp(self):
    self.location = Location(name='Anywhere')
    self.location.save_location()
    
  def tearDown(self):
    Location.objects.all().delete()
    
  def test_instance(self):
    self.assertTrue(isinstance(self.location,Location))
  
  def test_save_method(self):
    self.location.save_location()
    locations= Location.objects.all()
    self.assertTrue(len(locations) > 0)
    
  def test_update_method(self):
    self.location.save_location()
    new_location="somewhere"
    self.location.update_location(self.location.id,new_location)
    update = Location.objects.get(name='somewhere')
    self.assertEquals(update.name,"somewhere")
    
  def test_delete_method(self):
    self.location.save_location()
    self.location.delete_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations) == 0)
    

#category testcase   
class CategoryTestCase(TestCase):
  #setup method
  def setUp(self):
    self.category = Category(name='Travel')
    self.category.save_category()
    
  def tearDown(self):
    Category.objects.all().delete()
    
  def test_instance(self):
    self.assertTrue(isinstance(self.category,Category))
  
  def test_save_method(self):
    self.category.save_category()
    categorys= Category.objects.all()
    self.assertTrue(len(categorys) > 0)
    
  def test_update_method(self):
    self.category.save_category()
    new_category="Animals"
    self.category.update_category(self.category.id,new_category)
    update = Category.objects.get(name='Animals')
    self.assertEquals(update.name,"Animals")
    
  def test_delete_method(self):
    self.category.save_category()
    self.category.delete_category()
    categorys = Category.objects.all()
    self.assertTrue(len(categorys) == 0)
    
#image testcase
class ImageTestCase(TestCase):
  #set up method
  def setUp(self):
    self.category = Category(name='Travel')
    self.category.save_category()
    
    self.location = Location(name='somewhere')
    self.location.save_location()
    
    self.image = Image(name='test',description='Image description test',category=self.category,location=self.location)
  
  
  def tearDown(self):
    Image.objects.all().delete()
    Category.objects.all().delete()
    Location.objects.all().delete() 
     
  def test_instance(self):
    self.assertTrue(isinstance(self.image,Image))
    
  def test_save_method(self):
    self.image.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images)>0)
    
  def test_update_method(self):
    self.image.save_image()
    self.image.update_image(self.image.id,'images/test.jpg')
    new_image = Image.objects.filter(picture='images/test.jpg')
    self.assertTrue(len(new_image)>0)
    
  def test_delete_method(self):
    self.image.delete_image()
    images = Image.objects.all()
    self.assertTrue(len(images)== 0)
  
  def test_get_image_by_id(self):
    self.image.save_image()
    image_found=self.image.get_image_by_id(self.image.id)
    self.assertTrue(len(image_found)>0)
    
  def test_search_image_by_category(self):
    self.image.save_image()
    searched_image = self.image.search_by_category('Travel')
    self.assertTrue(len(searched_image) == 1)
    
  def test_filter_by_location(self):
    self.image.save_image()
    filtered_images = self.image.filter_by_location(location='somewhere')
    self.assertTrue(len(filtered_images) == 1)