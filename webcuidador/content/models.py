from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.

class Topico(models.Model):
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Creado_por')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    imagen = models.ImageField(verbose_name='Imagen', upload_to="topicos")
    url_infografia = models.URLField(null=True,verbose_name="URL Infografía")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Tópico'
        verbose_name_plural = 'Tópicos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

'''class Seccion(models.Model):
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Creado_por')
    topicos = models.ManyToManyField(Topico, verbose_name='Tópicos', blank=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.TextField(max_length=300, verbose_name='Descripción')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
'''
class Subtopico(models.Model):
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Creado_por')
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, verbose_name='Tópico')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    imagen = models.ImageField(verbose_name='Imagen', null=True, upload_to="subtopicos")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Subtópico'
        verbose_name_plural = 'Subtópicos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Tema(models.Model):
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Creado_por')
    subtopico = models.ForeignKey(Subtopico, on_delete=models.CASCADE, default=None, blank=True, null=True, verbose_name='Subtópico')
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, verbose_name='Tópico')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    imagen = models.ImageField(verbose_name='Imagen', null=True, upload_to="temas")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'
        ordering = ['topico', 'subtopico']

    def __str__(self):
        return self.nombre + ' --- Subtópico: ' + str(self.subtopico) + ' --- Tópico: ' + str(self.topico)

class DetalleTema(models.Model):
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Creado_por')
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, default=None, blank=True, null=True, verbose_name='Tema')
    subtopico = models.ForeignKey(Subtopico, on_delete=models.CASCADE, default=None, blank=True, null=True, verbose_name='Subtópico')
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, verbose_name='Tópico')
    descripcion = RichTextField(default="",verbose_name='Descripción')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Detalle de Tema'
        verbose_name_plural = 'Detalle de Temas'
        ordering = ['topico']

    def __str__(self):
        return self.descripcion


