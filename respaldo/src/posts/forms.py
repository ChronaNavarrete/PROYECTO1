from django import forms
from .models import Post, Comment, Profile
from django.forms import ModelForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author','categoria','concepto','content','thumbnail','slug']   #('__all__')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'concepto': forms.Select(attrs={'class':'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('content',)
