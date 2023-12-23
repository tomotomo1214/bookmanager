from django import forms
from .models import Book,Bookshelf
class PostForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=[
            'title',
            'detail',
            'bookshelf'
        ]
        model=Bookshelf
        fields=[
            'place'
        ]