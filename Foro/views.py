from django.shortcuts import render
from django.views.generic.edit import UpdateView
from Foro.forms import *
from PIL import Image as PImage
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from Foro.util import redir
from SitioWeb.settings import MEDIA_URL


# Create your views here.

class HomeForo(ListView):
    model = Foro
    template_name = "listaForos.html"
    paginate_by = 20

    def get_queryset(self):
        return Foro.objects.all()


class ListaTemas(ListView):
    model = Tema
    template_name = "listaTemas.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(ListaTemas, self).get_context_data()
        context['foro'] = Foro.objects.filter(id=self.kwargs.get('pk'))[0]
        context['lista_temas'] = Tema.objects.filter(foro=self.kwargs.get('pk'))
        return context


class ListaMensajes(ListView):
    model = Mensaje
    template_name = "listaMensajes.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(ListaMensajes, self).get_context_data()
        context['tema'] = Tema.objects.filter(id=self.kwargs.get('pk'))[0]
        context['lista_mensajes'] = Mensaje.objects.filter(tema=self.kwargs.get('pk'))
        context['media_url'] = MEDIA_URL
        return context


class DetalleUsuario(DetailView):
    model = PerfilUsuario


class EditarPerfil(UpdateView):
    model = PerfilUsuario
    form_class = FormPerfil
    success_url = "#"
    template_name = "perfil.html"

    def form_valid(self, form):
        """Resize and save profile image."""
        # remove old image if changed
        name = form.cleaned_data.get("avatar")
        pk = self.kwargs.get("pk")
        old = PerfilUsuario.objects.get(pk=pk).avatar

        if old.name and old.name != name:
            old.delete()

        # save new image to disk & resize new image
        self.form_object = form.save()

        if self.form_object.avatar:
            img = PImage.open(self.form_object.avatar.path)
            img.thumbnail((160, 160), PImage.ANTIALIAS)
            img.save(img.filename, "JPEG")

        return redir(self.success_url)


class EditarUsuario(UpdateView):
    model = User
    form_class = EditUserForm
    template_name = "editarUsuario.html"

    def get_success_url(self):
        return reverse_lazy('editar_perfil', args=(self.object.id,))
