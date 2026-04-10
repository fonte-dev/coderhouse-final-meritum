from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=150)

    cuerpo = RichTextField()

    imagen = models.ImageField(upload_to="articulos_imagenes/", null=True, blank=True)

    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor.username}"
