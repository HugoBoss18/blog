# publicaciones/urls.py
from django.urls import path

from .views import (
    VistaCrearPublicacion,
    VistaDetallePublicacion,
    VistaEditarPublicacion,
    VistaEliminarPublicacion,
    VistaInicio,
)

urlpatterns = [
    path("publicacion/nueva/", VistaCrearPublicacion.as_view(), name="publicacion_nueva"),
    path("publicacion/<int:pk>/", VistaDetallePublicacion.as_view(), name="publicacion_detalle"),
    path("publicacion/<int:pk>/editar/", VistaEditarPublicacion.as_view(), name="publicacion_editar"),
    path("publicacion/<int:pk>/eliminar/", VistaEliminarPublicacion.as_view(), name="publicacion_eliminar"),
    path("", VistaInicio.as_view(), name="inicio"),
]