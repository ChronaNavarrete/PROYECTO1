from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('content', )
    


'''sql 
    id
    etiquetas = conceptos = temas constitucionales # filtar el archivo bachele 2016
    nombre
    fecha
    hora
    #link
    realizado True False
    conclusion = str
    aprobacion = %
'''

