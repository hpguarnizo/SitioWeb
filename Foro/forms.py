__author__ = 'renatto'

from django.forms import ModelForm
from.models import *
from registration.forms import RegistrationFormUniqueEmail
from django import forms


class FormPerfil(ModelForm):
    class Meta:
        model   = PerfilUsuario
        exclude = ["mensajes", "user"]


class RegistrationForm(RegistrationFormUniqueEmail):
    attrs_dict = { 'class': 'required' }

    error_messages = {
        'password_mismatch': "Las contraseñas no coinciden.",
    }

    error_username={
        'invalid':'Solo puede contener letras, números y guiones bajos',
        'required':'Debe ingresar su nombre de usuario'
    }

    error_email={
        'invalid':'Ingrese una dirección de corro electrónico válida',
        'required':'Debe ingresar su dirección de correo electrónico'
    }

    error_password1={
        'required':'Debe ingresar una contraseña'
    }

    error_password2={
        'required':'Debe repetir su contraseña'
    }

    error_nombre={
        'required':'Debe ingresar su nombre'
    }

    error_apellido={
        'required':'Debe ingresar sus apellidos'
    }

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError("Esta dirección de correo está en uso. Por favor ingrese una dirección diferente.")
        return self.cleaned_data['email']


    username = forms.RegexField(regex=r'^\w+$', max_length=30,
                            widget=forms.TextInput(attrs=attrs_dict),
                            label="Nombre de usuario",
                            error_messages=error_username)

    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,maxlength=75)),
                             label="Correo electrónico",error_messages=error_email)

    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                            label="Contraseña:",error_messages=error_password1)

    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                            label="Repita su contraseña:",error_messages=error_password2)


