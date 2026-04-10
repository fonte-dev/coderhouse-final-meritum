from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Articulo
from django.db.models import Q


def inicio(request):
    return render(request, "pages/inicio.html")


def acerca_de(request):
    return render(request, "pages/acerca_de.html")


class ArticuloListView(ListView):
    model = Articulo
    template_name = "pages/articulo_list.html"
    context_object_name = "articulos"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(titulo__icontains=query) | Q(subtitulo__icontains=query)
            )
        return queryset


class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ["titulo", "subtitulo", "cuerpo", "imagen"]
    template_name = "pages/articulo_form.html"
    success_url = reverse_lazy("articulos")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = "pages/articulo_detail.html"
    context_object_name = "articulo"


class ArticuloUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    fields = ["titulo", "subtitulo", "cuerpo", "imagen"]
    template_name = "pages/articulo_form.html"
    success_url = reverse_lazy("articulos")

    def test_func(self):
        articulo = self.get_object()
        return self.request.user == articulo.autor


class ArticuloDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulo
    template_name = "pages/articulo_confirm_delete.html"
    success_url = reverse_lazy("articulos")

    def test_func(self):
        articulo = self.get_object()
        return self.request.user == articulo.autor
