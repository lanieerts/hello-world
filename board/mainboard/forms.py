from django.forms import ModelForm
from django import forms
from mainboard.models import *

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'title', 'contents', 'url', 'email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']
