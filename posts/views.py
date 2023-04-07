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
        'posts' : data
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
    success_url = reverse_lazy('posts-create')
    def form_valid(self,form):
        form.instance.author = self.request.user
        # message so feedback
        messages.success(self.request,'Your post was created successfully')
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


class PostUpdateView(UpdateView):
    model = Post
    fields = ['altText']
    success_url = reverse_lazy('posts-create')
    template_name = 'posts/post_update.html'
    def form_valid(self,form):
        form.instance.author = self.request.user
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
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})

    


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
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
  

