from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.models import User


@login_required
def bandeja_entrada(request):
    mensajes = Mensaje.objects.filter(receptor=request.user)
    return render(request, "messages_app/bandeja.html", {"mensajes": mensajes})


@login_required
def enviar_mensaje(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)

        form.fields["receptor"].queryset = User.objects.exclude(id=request.user.id)

        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            messages.success(request, "¡Mensaje enviado con éxito!")
            return redirect("bandeja")
    else:
        form = MensajeForm()

        form.fields["receptor"].queryset = User.objects.exclude(id=request.user.id)

    return render(request, "messages_app/enviar.html", {"form": form})
