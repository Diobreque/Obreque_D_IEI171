from django import forms
from .models import Socio

class FormSocios(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'
