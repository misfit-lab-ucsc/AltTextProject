# where we will create first form where inherits from user creation form

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Profile, User

# when we create a user or register on our app
class UserRegisterForm(UserCreationForm):
    # dont forget we can edit param
    email = forms.EmailField()
    is_staff = False # disallow access /admin by default

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already taken')
        return username

# update User model
class UserUpdateForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.user = UserRegisterForm(*args,**kwargs)

    def clean_username(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        if username:
            self.user.cleaned_data = cleaned_data
            self.user.clean_username()
        return username

    class Meta:
        model = User
        fields = ['username']

# update profile image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']



