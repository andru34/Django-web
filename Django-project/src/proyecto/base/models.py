from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tarea(models.Model):
    usuario = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=False,
                                blank=False)
    titulo = models.CharField(max_length=250, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['completo']
