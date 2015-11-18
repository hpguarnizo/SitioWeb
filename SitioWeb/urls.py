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
from Foro.forms import RegistrationForm,FormularioAutenticacion
from registration.backends.default.views import RegistrationView
from django.contrib.auth.decorators import login_required as LR
from Foro.views import EditarPerfil,DetalleUsuario
from django.conf.urls.static import  static
from SitioWeb.settings import MEDIA_URL,MEDIA_ROOT





urlpatterns = [

     url(r'^$', 'Foro.views.home', name='home'),
     url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        name='auth_login',
        kwargs={'authentication_form':FormularioAutenticacion }
    ),

    url(r'accounts/register/$',
        RegistrationView.as_view(form_class = RegistrationForm),
        name = 'registration_register'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^editperfil/(?P<pk>\d+)/$' , LR(EditarPerfil.as_view()), {}, name="editar_perfil"),
    url(r'^perfil/(?P<pk>\d+)/', LR(DetalleUsuario.as_view(template_name='perfil.html')), name="perfil")

]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)