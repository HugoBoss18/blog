# publicaciones/models.py
from django.conf import settings
from django.db import models
from django.urls import reverse


class Publicacion(models.Model):
    titulo = models.CharField(
        "título", max_length=200, help_text="Máximo 200 caracteres."
    )
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField("fecha de publicación", auto_now_add=True)

    class Meta:
        ordering = ["-fecha"]
        verbose_name = "publicación"
        verbose_name_plural = "publicaciones"

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("publicacion_detalle", kwargs={"pk": self.pk})