from django.contrib import admin
from django.urls import path, include
from . import views

# import our views here
from .views import (PostCreateView)

urlpatterns = [
    path('',views.home, name='posts-home'),
    # about page
    path('about/',views.about,name='posts-about'),
    # add ability to post
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    # update
    # path(),
    # delete
    # path(),
    # see and list post
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
