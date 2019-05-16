from django import forms
from .models import Alojamiento

class AlojamientoForm(forms.ModelForm):
    class Meta:
        model = Alojamiento
        fields = ['state', 'town', 'address', 'type', 'category']
        widgets = {
            'state': forms.TextInput(attrs={}),
            'town': forms.TextInput(attrs={}),
            'address': forms.TextInput(attrs={}),
            'type': forms.TextInput(attrs={}),
            'category': forms.TextInput(attrs={}),
}