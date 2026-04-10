from django.shortcuts import render, redirect
from .forms import RegistroFormulario, UserEditForm, AvatarUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Avatar


def registro(request):
    if request.method == "POST":
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "¡Cuenta creada con éxito! Ya podés iniciar sesión."
            )
            return redirect("login")
    else:
        form = RegistroFormulario()

    return render(request, "accounts/registro.html", {"form": form})


@login_required
def perfil(request):
    avatar_url = None
    if hasattr(request.user, "avatar") and request.user.avatar.imagen:
        avatar_url = request.user.avatar.imagen.url

    return render(request, "accounts/perfil.html", {"avatar_url": avatar_url})


@login_required
def editar_perfil(request):
    avatar, created = Avatar.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        avatar_form = AvatarUpdateForm(request.POST, request.FILES, instance=avatar)

        if user_form.is_valid() and avatar_form.is_valid():
            user_form.save()
            avatar_form.save()
            messages.success(request, "¡Tu perfil se actualizó correctamente!")
            return redirect("perfil")

    else:
        user_form = UserEditForm(instance=request.user)
        avatar_form = AvatarUpdateForm(instance=avatar)

    return render(
        request,
        "accounts/editar_perfil.html",
        {"user_form": user_form, "avatar_form": avatar_form},
    )
