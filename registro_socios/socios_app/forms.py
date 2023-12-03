from django import forms
from .models import Socio
# from django.core import validators
from socios_app.models import selector_estado, selector_sexo

class FormSocios(forms.ModelForm):
    nombre_socio = forms.CharField()
    fecha_incorporacion = forms.DateField(input_formats=['%Y-%m-%d'])
    anio_nacimiento = forms.DateField(input_formats=['%Y-%m-%d'])
    telefono = forms.CharField(min_length=9, max_length=9)
    correo_electronico = forms.CharField()
    sexo = forms.ChoiceField(choices=selector_sexo)
    estado = forms.ChoiceField(choices=selector_estado)
    observacion = forms.CharField(required=False)

    nombre_socio.widget.attrs['class'] = 'form-control'
    fecha_incorporacion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), input_formats=['%Y-%m-%d'])
    anio_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), input_formats=['%Y-%m-%d'])
    telefono.widget.attrs['class'] = 'form-control'
    correo_electronico.widget.attrs['class'] = 'form-control'
    sexo.widget.attrs['class'] = 'form-select'
    estado.widget.attrs['class'] = 'form-select'
    observacion.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Socio
        fields = ['nombre_socio', 'fecha_incorporacion', 'anio_nacimiento', 'telefono', 'correo_electronico', 'sexo', 'estado', 'observacion']

    def clean_correo_electronico(self):
        inputEmail = self.cleaned_data['correo_electronico']
        if '@' not in inputEmail:
            raise forms.ValidationError('Esto no parece un correo.')
        return inputEmail

    def clean_nombre_socio(self):
        inputNombre = self.cleaned_data['nombre_socio']
        if len(inputNombre) > 80:
            raise forms.ValidationError('Solo se permiten 80 caracteres')
        return inputNombre