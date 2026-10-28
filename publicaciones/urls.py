# publicaciones/urls.py
from django.urls import path

from .views import VistaDetallePublicacion, VistaInicio

urlpatterns = [
    path("publicacion/<int:pk>/", VistaDetallePublicacion.as_view(), name="publicacion_detalle"),
    path("", VistaInicio.as_view(), name="inicio"),
]