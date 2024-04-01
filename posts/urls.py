from django.contrib import admin
from django.urls import path, include
from . import views

# import our views here
from .views import (PostCreateView,PostListView,PostDetailView,PostUpdateView,PostDeleteView)



urlpatterns = [
    path('',views.home, name='posts-home'),
    # about page
    path('about/',views.about,name='posts-about'),
    # add ability to post
    path('post/new/',PostCreateView.as_view(),name='posts-create'),
    # update
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='posts-update'),
    # delete
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='posts-delete'),
    # see post view detail view
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    #  list post
    path('post/',PostListView.as_view(),name='post-list'),
    # search posts view
    path('search/',views.search,name='search'),
    # upload page
    path('upload/',views.upload,name='posts-upload'),

]
