from django.contrib import admin
from .models import PerfilUsuario
from .forms import FormPerfil
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Register your models here.

class PerfilAdmin(admin.ModelAdmin):
    #Split devuelve un arreglo
    #Lo que se busca es que en la vista del sitio de administración
    #Se muetres los siguientes a tributos del Perfil
    list_display = "user  mensajes  actualizacion".split()
    form=FormPerfil




def create_user_profile(sender, **kwargs):
    #Crear perfil cuando creamos usuario
    user = kwargs["instance"]
    if not PerfilUsuario.objects.filter(user=user):
        PerfilUsuario(user=user).save()

#Agregar a la vista de administración
admin.site.register(PerfilUsuario,PerfilAdmin)
post_save.connect(create_user_profile, sender=User)
