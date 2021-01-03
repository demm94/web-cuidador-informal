from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_cuidador', 'is_medico', 'password1', 'password2')

    #  Validación formulario de registro de usuario
    def clean(self):
        super(SignUpForm, self).clean()

        is_cuidador = self.cleaned_data.get('is_cuidador')
        is_medico = self.cleaned_data.get('is_medico')

        if is_medico == is_cuidador:
            self._errors['is_medico'] = self.error_class([ 'Debes registrarte como médico o cuidador.'])

        return self.cleaned_data
