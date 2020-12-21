from django.forms import ModelForm 
from django import forms

from cabildos.models import Cabildo

class CrearCabildo(forms.ModelForm):

    class Meta:
        model = Cabildo
        fields = ['categoria','concepto','nombre','fecha','link']
        widgets = {
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'concepto': forms.Select(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control'}),
            'link': forms.TextInput(attrs={'class':'form-control'}),
        }

