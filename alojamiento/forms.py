from django import forms
from .models import Alojamiento

class AlojamientoForm(forms.ModelForm):
    class Meta:
        model = Alojamiento
        fields = ['provincia', 'localidad', 'direccion', 'tipo_alojamiento', 'cant_estrellas']
        widgets = {
            'provincia': forms.TextInput(attrs={}),
            'localidad': forms.TextInput(attrs={}),
            'direccion': forms.TextInput(attrs={}),
            'tipo_alojamiento': forms.TextInput(attrs={}),
            'cant_estrellas': forms.NumberInput(attrs={}),
}