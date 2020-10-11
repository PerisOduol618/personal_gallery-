from django.test import TestCase
from .models import Photos, Location, Category

# Testing the save method


class LocationTestClass(TestCase):

    # set up method

    def setUp(self):
        self.Kinoo = Location(location_name='Kinoo')
 
    def test_instance(self):
        self.assertTrue(isinstance(self.Kinoo, Location))

    def test_save_method(self):
        self.Kinoo.save_location_name()

    # def test_delete_method(self):
    #     self.Kinoo.delete_location_name()

    


class PhotosTestClass(TestCase):
    def setUp(self):
        self.car_photo = Photos(photo_name ='Benz' , photo_description= 'My car' , photo_location ='Nairobi' photo_category ='cars' photo ='image.jpeg')

        #Create a new tag and dsaving it 
        self.new_photo = photo(name = )


