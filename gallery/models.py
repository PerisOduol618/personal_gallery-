from django.db import models

class Photos(models.Model):
    photo_name =models.CharField(max_length = 30)
    photo_description = models.TextField()
    photo_location = models.ForeignKey('Location', on_delete=models.SET_NULL, default = '', null=True)
    photo_category = models.ForeignKey('Category', on_delete=models.CASCADE, default='')
    photo = models.ImageField(upload_to = 'images/', default='image.jpg')

    def __str__(self):
        return self.photo_name
    
    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.save()
    
    
class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name

    def save_location_name(self):
        self.save()

    def delete_location_name(self):
        self.delete()

    
    
 

class Category(models.Model):
    category_name = models.CharField(max_length = 30)

    def save_category_name(self):
        self.save()

    def delete_category_name(self):
        self.delete()


    def __str__(self):
        return self.category_name

