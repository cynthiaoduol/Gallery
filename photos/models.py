from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image = models.ImageField(upload_to = 'images/',default='')
    # image_location = models.ForeignKey(Location)
    # image_category = models.ForeignKey(Category)


    def save_image(self):
        self.save()

    def __str__(self):
        return self.image_name


class Category(models.Model):
    category_name = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.category_name


class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        self.save()

    def __str__(self):
        return self.location_name
