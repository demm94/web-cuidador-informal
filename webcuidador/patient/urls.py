from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info_paciente, name='info_paciente'),
    path('info/registrar/', views.registrar_paciente, name='registrar_paciente'),
    path('info/sintomas/registrar/', views.registrar_sintoma, name='registrar_sintoma'),
]