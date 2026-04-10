from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("about/", views.acerca_de, name="acerca_de"),
    path("pages/", views.ArticuloListView.as_view(), name="articulos"),
    path(
        "pages/<int:pk>/", views.ArticuloDetailView.as_view(), name="articulo_detalle"
    ),
    path(
        "pages/<int:pk>/editar/",
        views.ArticuloUpdateView.as_view(),
        name="articulo_editar",
    ),
    path(
        "pages/<int:pk>/eliminar/",
        views.ArticuloDeleteView.as_view(),
        name="articulo_eliminar",
    ),
    path("pages/nuevo/", views.ArticuloCreateView.as_view(), name="articulo_crear"),
]
