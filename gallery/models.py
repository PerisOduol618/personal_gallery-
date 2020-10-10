from django.db import models

class Photos(models.Model):
    photo_name =models.CharField(max_length = 30)
    photo_description = models.TextField()
    Photo = models.ImageField(upload_to = 'images/',default='image.jpg')
    photo_location = models.ForeignKey('Location',default = '')
    photo_category = models.ForeignKey('Category',default='')

    def __str__(self):
        return self.photo_name


class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name


class Category(models.Model):
    category_name = models.CharField(max_length = 30)


    def __str__(self):
        return self.category_name
