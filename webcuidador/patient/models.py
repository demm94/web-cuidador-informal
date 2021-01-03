from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

estados = {("Soltero", "Soltero(a)"), ("Casado", "Casado(a)"), ("Viudo", "Viudo(a)")}

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

class Cuidador(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    edad = models.PositiveIntegerField(verbose_name='Edad')
    estado_civil = models.CharField(max_length=10, verbose_name='Estado Civil')
    tipo = models.CharField(max_length=10, verbose_name="Tipo de Cuidador")
    relacion_paciente = models.CharField(max_length=20, verbose_name="Relación con paciente")
    fecha_cuidado = models.DateField(verbose_name="Inicio de cuidados")

    class Meta:
        verbose_name = 'Cuidador'
        verbose_name_plural = 'Cuidadores'

    def __str__(self):
        return self.user.username

class TipoTest(models.Model):
    nombre = models.CharField(max_length=25, verbose_name="Nombre Test")

    class Meta:
        verbose_name = 'Tipo de Test'
        verbose_name_plural = 'Tipos de Test'

    def __str__(self):
        return self.nombre

class Test(models.Model):
    cuidador = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE, null=False, blank=False)
    tipo_test = models.ForeignKey(TipoTest, on_delete=models.CASCADE, null=False, blank=False)
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de realización')

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'
        ordering = ['-fecha']
    
    def __str__(self):
        return "ID: " + str(self.id)

class RespuestaNPI(models.Model):
    test = models.OneToOneField(Test, on_delete=models.CASCADE, null=False, blank=False)
    r1a = models.IntegerField(verbose_name="1a")
    r1b = models.IntegerField(verbose_name="1b", null=True, blank=True, default=0)
    r2a = models.IntegerField(verbose_name="2a")
    r2b = models.IntegerField(verbose_name="2b", null=True, blank=True, default=0)
    r3a = models.IntegerField(verbose_name="3a")
    r3b = models.IntegerField(verbose_name="3b", null=True, blank=True, default=0)
    r4a = models.IntegerField(verbose_name="4a")
    r4b = models.IntegerField(verbose_name="4b", null=True, blank=True, default=0)
    r5a = models.IntegerField(verbose_name="5a")
    r5b = models.IntegerField(verbose_name="5b", null=True, blank=True, default=0)
    r6a = models.IntegerField(verbose_name="6a")
    r6b = models.IntegerField(verbose_name="6b", null=True, blank=True, default=0)
    r7a = models.IntegerField(verbose_name="7a")
    r7b = models.IntegerField(verbose_name="7b", null=True, blank=True, default=0)
    r8a = models.IntegerField(verbose_name="8a")
    r8b = models.IntegerField(verbose_name="8b", null=True, blank=True, default=0)
    r9a = models.IntegerField(verbose_name="9a")
    r9b = models.IntegerField(verbose_name="9b", null=True, blank=True, default=0)
    r10a = models.IntegerField(verbose_name="10a")
    r10b = models.IntegerField(verbose_name="10b", null=True, blank=True, default=0)
    r11a = models.IntegerField(verbose_name="11a")
    r11b = models.IntegerField(verbose_name="11b", null=True, blank=True, default=0)
    r12a = models.IntegerField(verbose_name="12a")
    r12b = models.IntegerField(verbose_name="12b", null=True, blank=True, default=0)

    class Meta:
        verbose_name = 'Respuesta NPI'
        verbose_name_plural = 'Respuestas NPI'

class RespuestaZarit(models.Model):
    test = models.OneToOneField(Test, on_delete=models.CASCADE, null=False, blank=False)
    r1 = models.IntegerField(verbose_name="r1")
    r2 = models.IntegerField(verbose_name="r2")
    r3 = models.IntegerField(verbose_name="r3")
    r4 = models.IntegerField(verbose_name="r4")
    r5 = models.IntegerField(verbose_name="r5")
    r6 = models.IntegerField(verbose_name="r6")
    r7 = models.IntegerField(verbose_name="r7")
    r8 = models.IntegerField(verbose_name="r8")
    r9 = models.IntegerField(verbose_name="r9")
    r10 = models.IntegerField(verbose_name="r10")
    r11 = models.IntegerField(verbose_name="r11")
    r12 = models.IntegerField(verbose_name="r12")
    r13 = models.IntegerField(verbose_name="r13")
    r14 = models.IntegerField(verbose_name="r14")
    r15 = models.IntegerField(verbose_name="r15")
    r16 = models.IntegerField(verbose_name="r16")
    r17 = models.IntegerField(verbose_name="r17")
    r18 = models.IntegerField(verbose_name="r18")
    r19 = models.IntegerField(verbose_name="r19")
    r20 = models.IntegerField(verbose_name="r20")
    r21 = models.IntegerField(verbose_name="r21")
    r22 = models.IntegerField(verbose_name="r22")
    resultado = models.IntegerField(verbose_name="Resultado", default=None)
    evaluacion = models.CharField(max_length=50, verbose_name="Evaluación", default=None)

    class Meta:
        verbose_name = 'Respuesta Zarit'
        verbose_name_plural = 'Respuestas Zarit'
