from django.forms import ModelForm 
from django import forms

from cabildos.models import Cabildo

class CrearCabildo(ModelForm):
    class Meta:
        model = Cabildo
        fields = ['categoria','etiquetas','nombre','fecha','link']