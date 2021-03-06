from django.db.models import *
from django.contrib.auth.models import User
from django.conf import settings
from Foro.util import reverse2



class Foro(Model):
    titulo = CharField(max_length=60)
    descripcion = CharField(max_length=250)
    estado = BooleanField(default=1)

    # Nombre con el que figura en el sitio de administración
    # Es similar al metodo toString() de Java
    # Los métodos de la forma __xx__ son llamados por Python y no
    # a voluntad del programador :v
    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse2("temas", pk=self.pk)

    def num_temas(self):
        return self.temas.count()

    def num_mensajes(self):
        # Suma el número de mensajes en cada tema
        return sum([t.num_mensajes() for t in self.temas.all()])

    def ultimo_mensaje(self):
        # En la lista de temas encuentra el último mensaje
        temas = self.temas.all()
        ultimo = None
        for tema in temas:
            ultM = tema.ultimo_mensaje()
            if ultM and (not ultimo or ultM.fecha > ultimo.fecha):
                ultimo = ultM
        return ultimo


class Tema(Model):
    titulo = CharField(max_length=60)
    fecha = DateTimeField(auto_now_add=True)
    autor = ForeignKey(User, blank=True, null=True)
    foro = ForeignKey(Foro, related_name="temas")
    estado = BooleanField(default=1)

    class Meta:
        # Orden descendiente de acuerdo  la fecha
        ordering = ["-fecha"]

    def __str__(self):
        # Realiza una substitución en el String
        return str(self.id)

    def get_absolute_url(self):
        return reverse2("mensajes", pk=self.pk)

    def num_mensajes(self):
        return self.mensajes.count()

    def ultimo_mensaje(self):
        # Si hay mensajes---
        # Mensaje tiene una relación con Tema, esta relación es denominada
        # "mensajes" tema=ForeignKey(Tema,related_name="mensajes")
        # self.mensaje hace alusión a los mensajes que contiene un tema
        if self.mensajes.count():
            # Retorna el último mensaje
            # Ordena de forma descendente y toma el primer elemento
            return self.mensajes.order_by("-fecha")[0]

    # No se cuenta el mensaje inicial con el que empezó el tema
    def num_respuestas(self):
        return self.mensajes.count() - 1


class Mensaje(Model):
    fecha = DateTimeField(auto_now_add=True)
    actualizacion = DateTimeField(auto_now=True)
    # El nombre de la relación es usado para referenciar el atributo
    tema = ForeignKey(Tema, related_name="mensajes")
    autor = ForeignKey(User, blank=True, null=True)
    contenido = TextField(max_length=10000)
    # En python True=1
    apropiado = BooleanField(default=1)
    editado = BooleanField(default=0)

    class Meta:
        ordering = ["fecha"]

    def __str__(self):
        return str("%s - %s " % (self.autor, self.tema))

    def profile_data(self):
        p = self.autor.perfil
        return p.mensajes, p.avatar

    def getContenido(self):
        cont=self.contenido.replace("[q]","<div class='cita'>")
        cont=cont.replace("[/q]","</div>")
        return cont

class PerfilUsuario(Model):
    avatar = ImageField("Foto de perfil", upload_to="imagenes/", blank=True, null=True)
    mensajes = IntegerField(default=0)
    # Foreign Key con caracter de unicidad
    user = OneToOneField(User, related_name="perfil")
    # Fecha de actualización
    actualizacion = DateTimeField(auto_now=True)

    # La clave es manejada por la tabla User de django

    def __str__(self):
        return str(self.user)

    def incrementar_mensaje(self):
        self.mensajes += 1
        self.save()

    def imagen_avatar(self):
        # Si existe un avatar recuperarlo
        # Sino retornar None
        return (settings.MEDIA_URL + self.avatar.name) if self.avatar else None
