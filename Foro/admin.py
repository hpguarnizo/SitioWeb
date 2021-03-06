from django.contrib import admin
from .models import PerfilUsuario
from .forms import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Register your models here.

class PerfilAdmin(admin.ModelAdmin):
    #Split devuelve un arreglo
    #Lo que se busca es que en la vista del sitio de administración
    #Se muetres los siguientes a tributos del Perfil
    list_display = "user  mensajes  actualizacion".split()
    form=FormPerfil


class ForoAdmin(admin.ModelAdmin):
    form=FormForo

class TemaAdmin(admin.ModelAdmin):
    form = FormTema

class MensajeAdmin(admin.ModelAdmin):
    form = FormMensaje

def create_user_profile(sender, **kwargs):
    #Crear perfil cuando creamos usuario
    user = kwargs["instance"]
    if not PerfilUsuario.objects.filter(user=user):
        PerfilUsuario(user=user).save()

#Agregar a la vista de administración
admin.site.register(PerfilUsuario,PerfilAdmin)
admin.site.register(Foro,ForoAdmin)
admin.site.register(Tema,TemaAdmin)
admin.site.register(Mensaje,MensajeAdmin)
post_save.connect(create_user_profile, sender=User)
