from django import forms
from .models import Pregunta


class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['pregunta']

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['respuesta']
        
    def clean(self):
        cleaned_data = super().clean()
        respuesta = cleaned_data.get('respuesta')
        if not respuesta:
            self.add_error('respuesta', 'La respuesta no puede estar vacía.')