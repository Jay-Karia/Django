from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title of your post'
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'author': forms.Select(attrs={
                'class': 'form-control'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write more about your post',
                'style': 'max-height: 15rem',
            }),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title of your post'
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write more about your post',
                'style': 'max-height: 15rem'
            }),
        }
