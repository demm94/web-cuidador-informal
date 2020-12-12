from django.contrib import admin
from .models import Paciente, Sintoma, Historial

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Sintoma)
admin.site.register(Historial)
