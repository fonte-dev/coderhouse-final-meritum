from django import forms
from .models import Mensaje


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ["receptor", "contenido"]
        labels = {"receptor": "Destinatario", "contenido": "Escribí tu mensaje acá"}
