from django import forms
from .models import Post, Comment, Profile
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author','categoria','concepto','content','thumbnail','slug']   #('__all__')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'concepto': forms.Select(attrs={'class':'form-control'}),
            'content': forms.TextInput(attrs={'class':'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
<<<<<<< HEAD
        fields =('content', )

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


=======
        fields =('content',)
>>>>>>> 48015f148258c1e74ca8504ec95a6ead0ae44b44
