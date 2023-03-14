from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
    # all of our data from db we created for alt text post
    data = Post.objects.all()
    # dictionary containing our data that will be passed to our HTML template
    context = {
        'images' : data
    }
    # redering our template
    return render(request,'posts/base.html',context)
