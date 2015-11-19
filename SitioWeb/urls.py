"""StioWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login
from registration.backends.default.views import RegistrationView
from django.contrib.auth.decorators import login_required as LR
from Foro.views import *
from django.conf.urls.static import  static
from SitioWeb.settings import MEDIA_URL,MEDIA_ROOT
from Foro.security import anonymous_required as AR




urlpatterns = [

     url(r'^$', HomeForo.as_view(), name='home'),

     url(r'^temas/(?P<pk>\d+)/$',ListaTemas.as_view(),name="temas"),
     url(r'^mensajes/(?P<pk>\d+)/$',ListaMensajes.as_view(),name="mensajes"),

     url(r'^accounts/login/$',
        AR(login),
        name='auth_login',
        kwargs={'authentication_form':FormularioAutenticacion }
    ),

    url(r'accounts/register/$',
        AR(RegistrationView.as_view(form_class = RegistrationForm)),
        name = 'registration_register') ,

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^editperfil/(?P<pk>\d+)/$' , LR(EditarPerfil.as_view()), {}, name="editar_perfil"),
     url(r'^edituser/(?P<pk>\d+)/$' , LR(EditarUsuario.as_view()), {}, name="editar_user"),


]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)