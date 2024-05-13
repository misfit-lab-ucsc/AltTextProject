from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
#class PermissionLevel(models.Model):
#    name = models.CharField(max_length=50)
#    description = models.TextField(blank = True)

#class MyUser(User):
#    permission_level = models.ForeignKey(PermissionLevel, on_delete=models.CASCADE)
#    
#    def save(self, *args, **kwargs):
#        if not self.pk: 
#            default_permission_level = PermissionLevel.objects.get(name='Base')
#            self.permission_level = default_permission_level
#        super().save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics')
    desc = models.TextField(max_length=150, default='')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
