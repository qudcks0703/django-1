from django import forms
from .models import *
from .widgets import CounterTextInput

from django_summernote.widgets import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name']
        widgets = {
            'name': CounterTextInput,
        }
