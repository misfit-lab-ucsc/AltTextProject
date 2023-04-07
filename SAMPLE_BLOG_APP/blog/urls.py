from django.urls import path
from . import views

from .views import (PostListView,
PostDetailView,
PostCreateView,
PostUpdateView,
PostDeleteView,
UserPostListView,
)

# . means current directory
# empty path as home page
# name because we want reverse lookup on route

# in future for new paths maybe create dictionary and iterate over url patterns appending
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    # django give ability add variables to route like id of post this url is for list of posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # url pattern for create new post
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # update view
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # delete view
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # about page
    path('about/',views.about,name='blog-about'),
    # list of user post
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts')
]

