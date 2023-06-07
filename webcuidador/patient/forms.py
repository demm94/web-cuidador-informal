from django import forms
from .models import Evento, Paciente, Historial, Sintoma, RespuestaNPI, RespuestaZarit, Cuidador

class PacienteForm(forms.ModelForm):
    class Meta:
       
        model =  Paciente
        fields =  ['nombres', 'apellidos', 'edad', 'fecha_de_nacimiento','sexo','enfermedades']
        # Agregar estilos al formulario 
        SEXO_CHOICES = (
             ('None', 'None'),
            ('Femenino', 'Femenino'),
            ('Masculino', 'Masculino'),
           
        )
        widgets = { 
            'nombres': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombres del paciente'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Apellidos del paciente'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Edad'}),
            'fecha_de_nacimiento': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control mb-2', 'type': 'date'}),
            'sexo': forms.Select(choices=SEXO_CHOICES, attrs={'class': 'form-control mb-2'}),
            'enfermedades': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enfermedades Crónicas'}),
        }   

class RegistroEventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['fecha','f_baño', 'f_alimentacion', 'f_sueño', 'animo','comentario']

        widgets = {
            'fecha': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control mb-2', 'type': 'date'}),
            'f_baño': forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Frecuencia de baño'}),
            'f_alimentacion': forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Frecuencia de alimentación'}),
            'f_sueño': forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Horas de sueño'}),
            'animo': forms.NumberInput(attrs={'type':'range', 'class': 'form-range', 'min': '1', 'max': '10'}),
            'comentario': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Otro sintoma inusual o caida'}),
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

class TestNPIForm(forms.ModelForm):
    RESPUETA_A_CHOICES = (
        (1, 'Sí'),
        (0, 'No'),
        (9, 'No sabe'),
    )
    RESPUETA_B_CHOICES = (
        (1, 'Leve'),
        (2, 'Moderado'),
        (3, 'Severo'),
        (9, 'No sabe'),
    )
    r1a = forms.ChoiceField(choices=RESPUETA_A_CHOICES, widget=forms.RadioSelect())
    r1b = forms.ChoiceField(choices=RESPUETA_B_CHOICES, widget=forms.RadioSelect(), required=False)
    r2a = forms.ChoiceField(choices=RESPUETA_A_CHOICES, widget=forms.RadioSelect())
    r2b = forms.ChoiceField(choices=RESPUETA_B_CHOICES, widget=forms.RadioSelect(), required=False)
    r3a = forms.ChoiceField(choices=RESPUETA_A_CHOICES, widget=forms.RadioSelect())
    r3b = forms.ChoiceField(choices=RESPUETA_B_CHOICES, widget=forms.RadioSelect(), required=False)
    r4a = forms.ChoiceField(choices=RESPUETA_A_CHOICES, widget=forms.RadioSelect())
    r4b = forms.ChoiceField(choices=RESPUETA_B_CHOICES, widget=forms.RadioSelect(), required=False)
    r5a = forms.ChoiceField(choices=RESPUETA_A_CHOICES, widget=forms.RadioSelect())
    r5b = forms.ChoiceField(choices=RESPUETA_B_CHOICES, widget=forms.RadioSelect(), required=False)
    r6a = forms.ChoiceField(choices=RESPUETA_A_CHOICES, widget=forms.RadioSelect())
    r6b = forms.ChoiceField(choices=RESPUETA_B_CHOICES, widget=forms.RadioSelect(), required=False)
    r7a = forms.ChoiceField(choices=RESPUETA_A_CHOICES, widget=forms.RadioSelect())
    r7b = forms.ChoiceField(choices=RESPUETA_B_CHOICES, widget=forms.RadioSelect(), required=False)
    r8a = forms.ChoiceField(choices=RESPUETA_A_CHOICES, widget=forms.RadioSelect())
    r8b = forms.ChoiceField(choices=RESPUETA_B_CHOICES, widget=forms.RadioSelect(), required=False)
    r9a = forms.ChoiceField(choices=RESPUETA_A_CHOICES, widget=forms.RadioSelect())
    r9b = forms.ChoiceField(choices=RESPUETA_B_CHOICES, widget=forms.RadioSelect(), required=False)
    r10a = forms.ChoiceField(choices=RESPUETA_A_CHOICES, widget=forms.RadioSelect())
    r10b = forms.ChoiceField(choices=RESPUETA_B_CHOICES, widget=forms.RadioSelect(), required=False)
    r11a = forms.ChoiceField(choices=RESPUETA_A_CHOICES, widget=forms.RadioSelect())
    r11b = forms.ChoiceField(choices=RESPUETA_B_CHOICES, widget=forms.RadioSelect(), required=False)
    r12a = forms.ChoiceField(choices=RESPUETA_A_CHOICES, widget=forms.RadioSelect())
    r12b = forms.ChoiceField(choices=RESPUETA_B_CHOICES, widget=forms.RadioSelect(), required=False)

    class Meta:
        model = RespuestaNPI
        fields = ['r1a', 'r1b', 'r2a', 'r2b', 'r3a', 'r3b', 'r4a', 'r4b', 'r5a', 'r5b', 'r6a', 'r6b', 'r7a', 'r7b', 'r8a', 'r8b'
        , 'r9a', 'r9b', 'r10a', 'r10b', 'r11a', 'r11b', 'r12a', 'r12b']

class TestZaritForm(forms.ModelForm):
    RESPUESTA_CHOICES = (
        (1, 'Nunca'),
        (2, 'Rara vez'),
        (3, 'Alguna vez'),
        (4, 'Bastantes veces'),
        (5, 'Casi siempre'),
    )

    r1 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect())
    r2 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r3 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r4 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r5 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r6 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r7 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r8 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r9 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r10 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r11 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r12 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r13 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r14 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r15 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r16 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r17 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r18 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r19 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r20 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r21 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))
    r22 = forms.ChoiceField(choices=RESPUESTA_CHOICES, widget=forms.RadioSelect(attrs={'style': 'display: inline-block'}))

    class Meta:
        model = RespuestaZarit
        fields = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15', 'r16'
        , 'r17', 'r18', 'r19', 'r20', 'r21', 'r22']

class CuidadorForm(forms.ModelForm):

    ESTADO_CIVIL_CHOICES = (
        ('Soltero', 'Soltero(a)'),
        ('Casado', 'Casado(a)'),
        ('Viudo', 'Viudo(a)'),
    )

    TIPO_CUIDADOR_CHOICES = (
        ('Formal', 'Formal'),
        ('Informal', 'Informal'),
    )

    RELACION_PACIENTE_CHOICES = (
        ('Esposo', 'Esposo(a)'),
        ('Hijo', 'Hijo(a)'),
        ('Hermano', 'Hermano(a)'),
        ('Otro', 'Otro'),
    )
    #estado_civil = forms.ChoiceField(choices=ESTADO_CIVIL_CHOICES, widget=forms.SelectMultiple())
    #tipo = forms.ChoiceField(choices=TIPO_CUIDADOR_CHOICES, widget=forms.SelectMultiple())
    #relacion_paciente = forms.ChoiceField(choices=RELACION_PACIENTE_CHOICES, widget=forms.SelectMultiple())

    class Meta:
        model =  Cuidador
        fields =  ['edad', 'estado_civil', 'tipo', 'relacion_paciente', 'fecha_cuidado']

        # Agregar estilos al formulario 
        ESTADO_CIVIL_CHOICES = (
            ('Soltero', 'Soltero(a)'),
            ('Casado', 'Casado(a)'),
            ('Viudo', 'Viudo(a)'),
        )

        TIPO_CUIDADOR_CHOICES = (
            ('Formal', 'Formal'),
            ('Informal', 'Informal'),
        )

        RELACION_PACIENTE_CHOICES = (
            ('Esposo', 'Esposo(a)'),
            ('Hijo', 'Hijo(a)'),
            ('Hermano', 'Hermano(a)'),
            ('Otro', 'Otro'),
        )

        widgets = { 
            'edad': forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Ingrese Edad', 'pattern': "[0-9]*"}),
            'estado_civil': forms.Select(choices=ESTADO_CIVIL_CHOICES, attrs={'class': 'form-control mb-2'}),
            'tipo': forms.Select(choices=TIPO_CUIDADOR_CHOICES, attrs={'class': 'form-control mb-2'}),
            'relacion_paciente': forms.Select(choices=RELACION_PACIENTE_CHOICES, attrs={'class': 'form-control mb-2'}),
            'fecha_cuidado': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control mb-2', 'type': 'date'}),
        }   