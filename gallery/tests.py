from django.test import TestCase
from .models import Photos, Location, Category

# Testing the save method


class LocationTestClass(TestCase):

    # set up method

    def setUp(self):
        self.Kinoo = Location(location_name='Kinoo')
        self.Kinoo.save_location_name()

   
 
    def test_instance(self):
        self.assertTrue(isinstance(self.Kinoo, Location))

    def test_save_method(self):
        self.Kinoo.save_location_name()
        Locations = Location.objects.all()
        print(Locations)
        self.assertTrue(len(Locations)==1)

    def test_delete_method(self):
        self.Kinoo.delete_location_name()
        Locations = Location.objects.all()
        print(Locations)
        self.assertTrue(len(Locations)==0)
        

    def tearDown(self):
        Location.objects.all().delete()

class PhotosTestClass(TestCase):
    def setUp(self):
        self. new_location = Location(location_name = 'Mombasa')
        self. new_location.save()

        self. new_category = Category(category_name = 'Adventure')
        self. new_category.save()

        self. new_car = Photos(photo_name = 'Benz', photo_description = 'Nice photo', photo_location = self.new_location, photo_category = self.new_category, photo = 'image.jpeg' )
        self.new_car.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_car, Photos))

    def test_save_car(self):
        self. new_car.save_image()
