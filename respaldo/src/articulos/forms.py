from django.forms import ModelForm 
from django import forms

from articulos.models import Articulo

class CrearArticulo(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = ['nombre','categoria','concepto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'concepto': forms.Select(attrs={'class':'form-control'}),
        }