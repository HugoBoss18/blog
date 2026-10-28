# publicaciones/views.py
from django.views.generic import DetailView, ListView

from .models import Publicacion


class VistaInicio(ListView):
    model = Publicacion
    template_name = "inicio.html"
    context_object_name = "publicaciones"


class VistaDetallePublicacion(DetailView):
    model = Publicacion
    template_name = "publicacion_detalle.html"
    context_object_name = "publicacion"