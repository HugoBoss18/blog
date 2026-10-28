# publicaciones/views.py
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # nuevo
from django.urls import reverse_lazy  # nuevo

from .models import Publicacion


class VistaInicio(ListView):
    model = Publicacion
    template_name = "inicio.html"
    context_object_name = "publicaciones"


class VistaDetallePublicacion(DetailView):
    model = Publicacion
    template_name = "publicacion_detalle.html"
    context_object_name = "publicacion"

class VistaCrearPublicacion(CreateView):  # nuevo
    model = Publicacion
    template_name = "publicacion_nueva.html"
    fields = ["titulo", "autor", "contenido"]

class VistaEditarPublicacion(UpdateView):  # nuevo
    model = Publicacion
    template_name = "publicacion_editar.html"
    fields = ["titulo", "contenido"]

class VistaEliminarPublicacion(DeleteView):  # nuevo
    model = Publicacion
    template_name = "publicacion_eliminar.html"
    success_url = reverse_lazy("inicio")