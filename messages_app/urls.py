from django.urls import path
from . import views

urlpatterns = [
    path("inbox/", views.bandeja_entrada, name="bandeja"),
    path("new/", views.enviar_mensaje, name="enviar_mensaje"),
]
