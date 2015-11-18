from django.shortcuts import render
from django.views.generic.edit import UpdateView
from Foro.models import *
from Foro.forms import FormPerfil
from PIL import Image as PImage
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView


# Create your views here.
def home(request):
    titulo="Bienvenido"
    if request.user.is_authenticated():
       titulo="Mi título %s" % (request.user)
    contex={
        "titulo":titulo,
    }
    return render(request, "base.html", contex)


class DetalleUsuario(DetailView):
    model = PerfilUsuario


def redir(to, *args, **kwargs):
    if not (to.startswith('/') or to.startswith("http://") or to.startswith("../") or to=='#'):
        to = reverse(to, args=args, kwargs=kwargs)
    return HttpResponseRedirect(to)

class EditarPerfil(UpdateView):
    model = PerfilUsuario
    form_class = FormPerfil
    success_url = "#"
    template_name = "editarPerfil.html"


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
