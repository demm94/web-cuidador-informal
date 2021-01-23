from .forms import SignUpForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

# Formulario de registro cuidador
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    # Redirecciona a registro satisfactorio
    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()

        # Modifica los campos del formulario en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        form.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Apellido'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Repite la contraseña'}) 
        return form