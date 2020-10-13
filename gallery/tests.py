from django.test import TestCase
from .models import Photos, Location, Category

# Testing the save method


class LocationTestClass(TestCase):

    # set up method

    def setUp(self):
        self.Kinoo = Location(location_name='Kinoo')
        self.Kinoo.save_location_name()


    def tearDown(self):
        Location.objects.all().delete()
 
    def test_instance(self):
        self.assertTrue(isinstance(self.Kinoo, Location))

    def test_save_method(self):
        self.Kinoo.save_location_name()
        Locations = Location.objects.all()
        print(Locations)
        self.assertTrue(len(Locations)==1)

    def test_update_location(self):
        new_location.update_location(self.location.id,new_location_name)
        updated_location = Location.objects.filter(location_name='Kasrani')
        self.assertTrue(len(updated_location) > 0)


    def test_delete_method(self):
        self.Kinoo.delete_location_name()
        Locations = Location.objects.all()
        print(Locations)
        self.assertTrue(len(Locations)==0)
        

    

class PhotosTestClass(TestCase):
    def setUp(self):
        self. new_location = Location(location_name = 'Mombasa')
        self. new_location.save()

        self. new_category = Category(category_name = 'Adventure')
        self. new_category.save()

        self. new_car = Photos(name = 'Benz', photo_description = 'Nice photo', photo_location = self.new_location, photo_category = self.new_category, photo = 'image.jpeg' )
        self. new_car.save()

    def tearDown(self):
        Photos.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_car, Photos))

    def test_save_car(self):
        self.new_car.save_photo()
        photo = Photos.objects.all()
      
        
    def test_delete_car(self):
        self.new_car.save_photo()
        self.new_car.delete_photo()
       

class CategoryTestClass(TestCase):
    def setUp(self):
        self.Tour= Category(category_name ='Tour')
        self.Tour.save_category_name()


    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.Tour, Category))

    def test_save_category(self):
        self.test_category = Category(category_name = 'Business')
        self.test_category.save_category_name()


    def test_delete_category(self):
        self.test_category = Category(category_name = 'Business')
        self.test_category.save_category_name()
        self.test_category.delete_category_name()






    
    