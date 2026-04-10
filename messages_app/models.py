from django.db import models
from django.contrib.auth.models import User


class Mensaje(models.Model):
    emisor = models.ForeignKey(
        User, related_name="mensajes_enviados", on_delete=models.CASCADE
    )

    receptor = models.ForeignKey(
        User, related_name="mensajes_recibidos", on_delete=models.CASCADE
    )

    contenido = models.TextField()

    fecha_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha_envio"]

    def __str__(self):
        return f"Mensaje de {self.emisor.username} para {self.receptor.username}"
