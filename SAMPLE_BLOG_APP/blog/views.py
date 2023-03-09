from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# add our post model to put our db data on page instead of jank dictionary
from .models import Post

# Create your views here.
# function handle traffic home page of our blog


# import list view, detail view 
from django.views.generic import (ListView,
DetailView,
CreateView,
UpdateView,
DeleteView)

# import our user
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    # dictionary to display posts to html
    context = {
        # reference data from our db
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# view to see list of post
class PostListView(ListView):
    # variable model tell list view what model query to make the list in this case post
    model = Post
    # <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    # use context refer line 14
    context_object_name = 'posts' 
    # change list view order add - 
    ordering = ['-date_posted']
    # paginate post to pages we dont need import just this property
    paginate_by = 5
    
# view to see user list of post
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts' 
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        # get user name from url if not return 404
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # we can filter query set
        return Post.objects.filter(author=user).order_by('-date_posted')
    
# view to see our post in detail
class PostDetailView(DetailView):
    model = Post

# view with form where we create new post what we need provide is fields in form like title and content
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    # over ride form valid method
    def form_valid(self,form):
        # saying that form trying to submit before do take instance set author set it to curretn logged in user 
        form.instance.author = self.request.user
        return super().form_valid(form)

    

# Instead of Creating for update
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        # get exact post that is being viewed
        post = self.get_object()
        # check if user has same name as author to aunthenticate
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        # get exact post that is being viewed
        post = self.get_object()
        # check if user has same name as author to aunthenticate
        if self.request.user == post.author:
            return True
        else:
            return False




def about(request):
    return render(request, 'blog/about.html' , {'title' : 'About'})