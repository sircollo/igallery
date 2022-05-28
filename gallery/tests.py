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