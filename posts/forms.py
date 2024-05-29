# This is where will implement search for posts in home screen

from django import forms
from .models import Post

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['photo','alt_text','tags']
    
    photo = forms.ImageField(required=True, label='Photo (2MB max):')
    
    alt_text = forms.CharField(required=True,
                               label='Alt Text:',
                               widget=forms.TextInput(attrs={'placeholder': 'Please accurately describe the image!'}))
    suggested_alt_text = ""

    tags = forms.CharField(required=True,
                           label='Tags (separate tags by comma):',
                           widget=forms.TextInput(attrs={'placeholder': 'Tag1, Tag2, Tag3, ...'}))
    suggested_tags = []