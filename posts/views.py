# import our models
from .models import Post

# import render to render our template 
from django.shortcuts import render, get_object_or_404

# import HttpResponse to return a response
from django.http import HttpResponse

# import Q object to do complex queries
from django.db.models import Q

# import reverse lazy to redirect to a specific page after creating a post
from django.urls import reverse_lazy
# import messages to give feedback to user
from django.contrib import messages

# import user and login mixin checking if user is logged in and if they are the author of the post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# pagination
from django.core.paginator import Paginator

# importing our forms
from .forms import SearchForm, PostForm

# import generic class based views that django has to offer
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

# importing random to get random posts
import random

# importing Pillow to resize images
from PIL import Image

# importing io to save image to memory
from io import BytesIO

# importing uploaded file to save image to memory
from django.core.files.uploadedfile import InMemoryUploadedFile

# importing os to get file extension
import os

# importing temporary uploaded file to save image to memory
from django.core.files.uploadedfile import TemporaryUploadedFile





# -----------------------------------------------------------------------------------------------
# Create your views here.
# -----------------------------------------------------------------------------------------------


# Register additional MIME types and file extensions
Image.register_mime('image/jpeg', '.jpg')
Image.register_mime('image/png', '.png')
Image.register_mime('image/gif', '.gif')

def home(request):
    # all of our data from db we created for alt text post
    all_posts = Post.objects.all()
    # check if there are at least 3 posts
    if len(all_posts) >= 3:
        # get 3 random posts
        random_posts = random.sample(list(all_posts), len(all_posts))
    else:
        # if there are less than 3 posts just get all posts
        random_posts = all_posts
    # dictionary containing our data that will be passed to our HTML template
    context = {
        'posts' : random_posts
    }
    # redering our template
    return render(request,'posts/base.html',context)

# about page
def about(request):
    return render(request,'posts/about.html',{'title' : 'About'})

# upload feature
def upload(request):
    return render(request,'posts/upload.html',{'title' : 'Upload'})

# howtoalttext page
def howtoalttext(request):
    return render(request,'posts/howtoalttext.html',{'title' : 'How to Alt Text'})

# help page
def help(request):
    return render(request,'posts/help.html',{'title' : 'Help'})

# search view we are going to do it based on alt text or title of post for now TBD / early stage
def search(request):
    # Check if request method is GET
    if request.method == 'GET':
        # getting our form to render in our template
        form = SearchForm(request.GET)
        # check if form is valid
        if form.is_valid():
            # get the query from the search bar
            query = form.cleaned_data.get('query')
            # if query is not None:
            if query:
                # if query is not empty meaning we have something to search for
                # filter Post objects by searching for alt text or title that contains our query
                results = Post.objects.filter(Q(alt_text__icontains=query) | Q(title__icontains=query)).distinct()
                
                # dictionary of our posts that we found that match query and what we searched for
                context = {
                    'posts': results,
                    'query': query,
                }
                
                # render search results template with context dictionary
                return render(request, 'posts/search_results.html', context)
        
        # if form is not valid
        else:
            form = SearchForm()
            query = ''
        
        # create context dictionary with empty form and query strings to avoid error
        context = {
            'form': form,
            'query': query,
        }
        
        # render search bar template with context dictionary
        return render(request, 'posts/search_results.html', context)



# view to create posts using class based views
# POST CREATE VIEW NEED TO HANDLE DIFFERENT IMAGE TYPES WHEN SAVING AND RESIZING
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    #fields = ['photo','alt_text','tags']
    success_url = reverse_lazy('posts-create')
    form_class = PostForm

    def form_valid(self,form):
        form.instance.author = self.request.user
        form.instance.tags = {"tags": form.instance.tags.split(',')}
        # message so feedback
        messages.success(self.request,'Your post was created successfully')
        # call the super method to save the form instance from the parent class
        return super().form_valid(form)
    
# WORK ON UPDATE LIST AND DELETE VIEW AS WELL AS UI FOR IT

# list view to see posts
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    # ordering posts
    ordering= ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['alt_text']
    # change this to post list to see list of posts to update Alt Text post-list
    success_url = reverse_lazy('posts-create')
    template_name = 'posts/post_update.html'
    def form_valid(self,form):
        form.instance.last_updated_by = self.request.user
        # pass the request object to the save method
        form.instance.save(request=self.request)
        # message so feedback
        messages.success(self.request,'Your post was updated successfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,'Your post was not updated successfully')
        return super().form_invalid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    def get_success_url(self):
        # 'post-detail', kwargs={'pk': self.object.pk}
        return reverse_lazy('posts-create')
    
# In charge of deleting posts
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# need to refactor and go back but this class or view handles the user posts
class UserPostListView(ListView):
    model = Post
    template_name = 'posts/user_posts.html'
    context_object_name = 'posts'
    # ordering posts
    ordering= ['-date_posted']
    paginate_by = 5
    def get_queryset(self): 
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
  

