"""AltText URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# for our images and static files
from django.conf import settings
from django.conf.urls.static import static

# need to add our user views to handle basic login functionality
from users import views as user_views
# handle login using django package
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # where we will have our alt text home page
    path('',include('posts.urls'),),
    # register new user
    path('register/',user_views.register,name='register'),
    # viewing our users profile
    path('profile/',user_views.profile,name='profile'),
    # logging in
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html',extra_context={'title':'Login'}),name='login'),
    # logging our user out 
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html',extra_context={'title':'Logout'}),name='logout'),
    # password reset views
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html',extra_context={'title':'Password Reset'}),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html',extra_context={'title':'Password Reset Done'}),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',extra_context={'title':'Password Reset Confirm'}),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html',extra_context={'title':'Password Reset Complete'}),name='password_reset_complete'),


] 
# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)