from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title of your post',
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'author': forms.Select(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(
                choices=choice_list,
                attrs={
                    'class': 'form-control',
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
        fields = ('title', 'title_tag', 'category', 'body')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title of your post'
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(
                choices=choice_list,
                attrs={
                    'class': 'form-control',
                }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write more about your post',
                'style': 'max-height: 15rem'
            }),
        }


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the name of the category',
                'style': "width:50%"
            }),
        }
