from django.test import TestCase
from .models import Photos,Location,Category

#Testing the save method 
class PhotosTestClass(TestCase):

    # set up method
    def setUp(self):
        self.photo_location = Location(location_name = 'Kinoo')
        self.photo_location.save()

    

    







