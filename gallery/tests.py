from django.test import TestCase
from .models import *
# Create your tests here.

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