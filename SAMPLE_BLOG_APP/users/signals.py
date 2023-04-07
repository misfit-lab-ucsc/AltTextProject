# this signal file will help create profile every time a user is created

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# when a user is saved then send this signal
# signal recieved by reciever and reciever is function that creates the profile
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# save profile function saves profile everytime user object is saved

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()