__author__ = 'renatto'

from django.forms import ModelForm
from.models import *
from registration.forms import RegistrationFormUniqueEmail
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User



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

error_password={
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


class FormPerfil(ModelForm):
    class Meta:
        model   = PerfilUsuario
        exclude = ["mensajes", "user"]


class FormForo(ModelForm):
    class Meta:
        model   = Foro
        fields= ['titulo']

class FormTema(ModelForm):
    class Meta:
        model   = Tema
        fields= "titulo autor foro".split()


class FormMensaje(ModelForm):
    class Meta:
        model   = Mensaje
        fields= "titulo tema autor contenido apropiado".split()



class RegistrationForm(RegistrationFormUniqueEmail):


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
                            label="Contraseña:",error_messages=error_password)

    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                            label="Repita su contraseña:",error_messages=error_password2)



class FormularioAutenticacion(AuthenticationForm):

    username = forms.RegexField(regex=r'^\w+$', max_length=30,
                            widget=forms.TextInput(attrs=attrs_dict),
                            label="Nombre de usuario",
                            error_messages=error_username)
    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                            label="Contraseña:",error_messages=error_password)

    error_messages = {
        'invalid_login': "Por favor ingrese un correcto %(username)s y contraseña. "
                           "Note que los campos pueden ser sensibles a mayúsculas.",
        'inactive': "Esta cuenta está inactiva.",
    }



class EditUserForm(forms.ModelForm):

     error_firstname={
        'invalid':'Solo puede contener letras y espacios',

      }

     class Meta:
        model = User
        fields = 'username','email','first_name','last_name'


     username = forms.RegexField(regex=r'^\w+$', max_length=30,
                            widget=forms.TextInput(),
                            label="Nombre de usuario",
                            error_messages=error_username)

     email = forms.EmailField(widget=forms.TextInput(attrs=dict(maxlength=75)),
                             label="Correo electrónico",error_messages={'invalid':'Ingrese una dirección de corro electrónico válida'})


     first_name = forms.RegexField(regex=r'^[a-zA-Z\s]*$', max_length=30,
                            widget=forms.TextInput(),
                            label="Nombres",
                            error_messages=error_firstname)

     last_name = forms.RegexField(regex=r'^[a-zA-Z\s]*$', max_length=30,
                            widget=forms.TextInput(),
                            label="Apellidos",
                            error_messages=error_firstname)

     def clean_email(self):
       email = self.cleaned_data['email']
       if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
          raise forms.ValidationError("Esta dirección de correo está en uso")
       return email


