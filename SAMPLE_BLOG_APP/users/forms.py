# where we will create first form where inherits from user creation form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # class meta gives nested name space for configuration and keep it in one space model being affected is user model fields we want and in order
    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']


# create model form - allows us to create form which allows us to work with specific db model in this case form update User model
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # class meta gives nested name space for configuration and keep it in one space model being affected is user model fields we want and in order
    class Meta:
        model = User
        fields = ['username', 'email']

# update our image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

