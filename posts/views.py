from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

from django.urls import reverse_lazy
from django.contrib import messages
# import user and login mixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# import generic class based views that django has to offer
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
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

# about page

def about(request):
    return render(request,'posts/about.html',{'title' : 'About'})

# view to create posts using class based views
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','photo','altText']
    success_url = reverse_lazy('posts-home')
    def form_valid(self,form):
        form.instance.author = self.request.user
        # message so feedback
        messages.success(self.request,'Your post was created successfully')
        return super().form_valid(form)
    
# WORK ON UPDATE LIST AND DELETE VIEW AS WELL AS UI FOR IT