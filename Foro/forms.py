__author__ = 'renatto'

from django.forms import ModelForm
from.models import *


class FormPerfil(ModelForm):
    class Meta:
        model   = PerfilUsuario
        exclude = ["mensajes", "user"]