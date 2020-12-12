from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

estados = {("Soltero(a)", "Soltero(a)"), ("Casado(a)", "Casado(a)")}

class Paciente(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=50, verbose_name='Nombres')
    apellidos = models.CharField(max_length=50, verbose_name='Apellidos')
    edad = models.PositiveIntegerField(verbose_name='Edad')
    estado_civil = models.CharField(max_length=10, default="Soltero", choices=estados, verbose_name='Estado Civil')

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

class Sintoma(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Síntoma'
        verbose_name_plural = 'Síntomas'

    def __str__(self):
        return self.nombre

class Historial(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False, blank=False)
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    sintomas = models.ManyToManyField(Sintoma, blank=False)
    comentario = models.TextField(max_length=200, default="", verbose_name="Comentario")

    class Meta:
        verbose_name = 'Historial'
        verbose_name_plural = 'Historiales'

    def __str__(self):
        return 'Registro' + ' ' + self.paciente.nombres
