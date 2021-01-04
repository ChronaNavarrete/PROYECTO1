from django.forms import ModelForm 
from django import forms

from cabildos.models import Cabildo, Cabildo_Online

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


class Cabildo_OnlineForm(ModelForm):
    class Meta:
        model = Cabildo_Online
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control'}),
            'hora': forms.TextInput(attrs={'class':'form-control'}),
            'link': forms.TextInput(attrs={'class':'form-control'}),
        }

