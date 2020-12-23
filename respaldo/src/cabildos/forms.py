from django.forms import ModelForm 
from django import forms

from cabildos.models import Cabildo, Cabildo_Online

class CrearCabildo(ModelForm):
    class Meta:
        model = Cabildo
        fields = '__all__'


class Cabildo_OnlineForm(forms.ModelForm):
    class Meta:
        model = Cabildo_Online
        fields = [
            'nombre',
            'fecha',
            'hora',
            'link',
        ]

       # labels = {
        #    'nombre' : 'Nombre',
         #   'fecha' : 'Fecha',
          #  'hora' : 'Hora',
           # 'link' : 'Link',
        #}

        #widgets = {
         #   'nombre' : forms.TextInput(attrs={'class':'form-control'}),
          # 'hora' : forms.TextInput(attrs={'class':'form-control'}),
            #'link' : forms.TextInput(attrs={'class':'form-control'}),
        #}