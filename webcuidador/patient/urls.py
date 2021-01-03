from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info_cuidador, name='info_cuidador'),
    path('info/registrar/', views.registrar_paciente, name='registrar_paciente'),
    path('info/registro_perfil/', views.registrar_perfil_cuidador, name='registrar_perfil_cuidador'),
    path('info/editar_perfil/<int:id_cuidador>/', views.editar_perfil_cuidador, name='editar_perfil_cuidador'),
    path('info/sintomas/registrar/', views.registrar_sintoma, name='registrar_sintoma'),
    path('info/test-npi/', views.test_npi, name='test_npi'),
    path('info/test-zarit/', views.test_zarit, name='test_zarit'),
]