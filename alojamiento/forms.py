from django import forms
from .models import Accommodation

class AlojamientoForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = ['state', 'town', 'address', 'type_code', 'category']
        widgets = {
            'state': forms.TextInput(attrs={}),
            'town': forms.TextInput(attrs={}),
            'address': forms.TextInput(attrs={}),
            'type_code': forms.TextInput(attrs={}),
            'category': forms.TextInput(attrs={}),
}