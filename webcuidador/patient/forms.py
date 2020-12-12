from django import forms
from .models import Paciente, Historial, Sintoma

class PacienteForm(forms.ModelForm):

    class Meta:
        model =  Paciente
        fields =  ['nombres', 'apellidos', 'edad', 'estado_civil']
        # Agregar estilos al formulario 
        widgets = { 
            'nombres': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de paciente'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de paciente'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Edad'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control mb-2'}),
        }   

class RegistroSintomaForm(forms.ModelForm):
    sintomas = forms.ModelMultipleChoiceField(
            label="Selecciona los síntomas",
            queryset=Sintoma.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=True)
    class Meta:
        model = Historial
        fields = ['sintomas', 'comentario']
        # Agregar estilos al formulario 
        widgets = { 
            'sintomas': forms.SelectMultiple(attrs={'class': 'form-control mb-2'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control mb-2', 'placeholder': 'Ingresa un comentario'}),
        }