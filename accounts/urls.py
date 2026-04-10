from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from . import views

urlpatterns = [
    path(
        "login/", LoginView.as_view(template_name="accounts/login.html"), name="login"
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),
    path("registro/", views.registro, name="registro"),
    path("profile/", views.perfil, name="perfil"),
    path("profile/edit/", views.editar_perfil, name="editar_perfil"),
    path(
        "password/",
        PasswordChangeView.as_view(
            template_name="accounts/cambiar_password.html",
            success_url="/accounts/profile/",
        ),
        name="cambiar_password",
    ),
]
