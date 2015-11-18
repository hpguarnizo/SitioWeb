from django.shortcuts import render



# Create your views here.
def home(request):
    titulo="Bienvenido"
    if request.user.is_authenticated():
       titulo="Mi título %s" % (request.user)
    contex={
        "titulo":titulo,
    }
    return render(request, "base.html", contex)




