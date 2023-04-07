from django.db import models
# extend existing user model django provide
from django.contrib.auth.models import User
# where we will config user and add profile pic
# Create your models here.

# import pillow librarry for image resizeing
from PIL import Image

# where add profile where profile pic
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # over ride save method of profile model to resize image
    # to add delete old images when new one is uplouded
    def save(self,*args, **kwargs):
        # first we need run save method of parent clases
        super().save(*args, **kwargs)
        # open imag of current instance
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            # resize image
            img.thumbnail(output_size)
            # save it 
            img.save(self.image.path)




