from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
# need think what we want save in db
# store users author of posts
# posts themselves
# each class own table in db
# each attribute different field in db

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # ondelete tell django if user create post then was deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # dunder method
    def __str__(self):
        return self.title
    # how find url to any specific instance of post
    def get_absolute_url(self):
        # reverse functon used generate url for named url pattern in this case its our post
        return reverse('post-detail',kwargs = {'pk': self.pk})