# This is where will implement search for posts in home screen

from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search')