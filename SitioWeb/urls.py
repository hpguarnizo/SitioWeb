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
from django.conf.urls.static import static
from SitioWeb.settings import MEDIA_URL, MEDIA_ROOT
from Foro.security import anonymous_required as AR
from django.views.generic.base import TemplateView

urlpatterns = [

    url(r'^$', HomeForo.as_view(), name='home'),
    url(r'^nuevotema/(?P<pk>\d+)/$', LR(NuevoTema), name='nuevo_tema'),
    url(r'^creartema/$', LR(CrearTema), name='crear_tema'),
    url(r'^temas/(?P<pk>\d+)/$', ListaTemas.as_view(), name="temas"),
    url(r'^mensajes/(?P<pk>\d+)/$',LR(ListaMensajes.as_view()), name="mensajes"),
    url(r'^nuevomensaje/(?P<pk>\d)/$',LR(NuevoMensaje), name="nuevo_mensaje"),
    url(r'^crearmensaje/$',LR(CrearMensaje), name="crear_mensaje"),
    url(r'^usuario/(?P<pk>\d+)/', LR(DetalleUsuario.as_view()), name="detalle_usuario"),
    url(r'^accounts/login/$', AR(login), name='auth_login', ),
    url(r'^temascreados/(?P<pk>\d+)/', LR(ListaTemasUsuario.as_view()), name="temas_creados"),
    url(r'^mensajescreados/(?P<pk>\d+)/', LR(ListaMensajesUsuario.as_view()), name="mensajes_creados"),
    url(r'^desactivar/$', LR(TemplateView.as_view(template_name = "foro/desactivarCuenta.html")), name="desactivar"),
    url(r'^activar/$', AR(TemplateView.as_view(template_name = "foro/activarCuenta.html")), name="activar"),
    url(r'^estado/$',LR(DesactivarCuenta) ,name='estado'),
    url(r'^actestado/$',AR(ActivarCuenta) ,name='estado_act'),

    url(r'^msjcensura/(?P<pk>\d+)/', LR(MensajeCensura), name="censura"),
    url(r'^confcensura/$', LR(ConfirmarCensura), name="conf_censura"),

    url(r'accounts/register/$',
        AR(RegistrationView.as_view(form_class=RegistrationForm)),
        name='registration_register'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^editperfil/(?P<pk>\d+)/$', LR(EditarPerfil.as_view()), {}, name="editar_perfil"),
    url(r'^edituser/(?P<pk>\d+)/$', LR(EditarUsuario.as_view()), {}, name="editar_user"),

    url(r'^summernote/', include('django_summernote.urls')),

    url(r'^prueba/$',prueba)

]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
