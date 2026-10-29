# publicaciones/views.py
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Publicacion


class VistaInicio(ListView):
    model = Publicacion
    template_name = "inicio.html"
    context_object_name = "publicaciones"


class VistaDetallePublicacion(DetailView):
    model = Publicacion
    template_name = "publicacion_detalle.html"
    context_object_name = "publicacion"

class VistaCrearPublicacion(LoginRequiredMixin, CreateView):
    model = Publicacion
    template_name = "publicacion_nueva.html"
    fields = ["titulo", "contenido"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class VistaEditarPublicacion(LoginRequiredMixin, UpdateView):
    model = Publicacion
    template_name = "publicacion_editar.html"
    fields = ["titulo", "contenido"]


class VistaEliminarPublicacion(LoginRequiredMixin, DeleteView):
    model = Publicacion
    template_name = "publicacion_eliminar.html"
    success_url = reverse_lazy("inicio")