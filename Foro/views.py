from django.shortcuts import render
from django.views.generic.edit import UpdateView
from Foro.forms import *
from PIL import Image as PImage
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from Foro.util import redir
import datetime

# Create your views here.
def home(request):
    now = datetime.datetime.now()
    fecha=now.strftime("%Y-%m-%d")

    contex={
        "fecha":fecha,
    }
    return render(request, "listaForos.html", contex)


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
        pk   = self.kwargs.get("pk")
        old  = PerfilUsuario.objects.get(pk=pk).avatar


        if old.name and old.name != name:
            old.delete()

        # save new image to disk & resize new image
        self.form_object = form.save()

        if self.form_object.avatar:
            img = PImage.open(self.form_object.avatar.path)
            img.thumbnail((160,160), PImage.ANTIALIAS)
            img.save(img.filename, "JPEG")


        return redir(self.success_url)


class EditarUsuario(UpdateView):
    model=User
    form_class=EditUserForm
    template_name = "editarUsuario.html"

    def get_success_url(self):
        return reverse_lazy('editar_perfil', args = (self.object.id,))





