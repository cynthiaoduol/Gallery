from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image = models.ImageField(upload_to = 'images/',default='')

    def save_image(self):
        self.save()

    def __str__(self):
        return self.image_name



