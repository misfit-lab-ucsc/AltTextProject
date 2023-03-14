from django.db import models
from PIL import Image
import os


# Create your models here.


class Post(models.Model):
    # Each post that the database will store
    # need to change max length property later
    title = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='pics')
    altText = models.TextField(max_length=20,default='Some String')

    # need to resize our posts need to override save method as well as use PILLOW
    # documented more in sample blog app folder
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.photo.path)
        # we will change the numbers later
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    
