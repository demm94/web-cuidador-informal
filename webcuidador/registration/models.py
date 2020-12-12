from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_medico = models.BooleanField(default=False, verbose_name='Médico')
    is_cuidador = models.BooleanField(default=False, verbose_name='Cuidador')
    is_gestionador = models.BooleanField(default=False, verbose_name='Gestionador')