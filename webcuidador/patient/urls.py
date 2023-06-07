from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info_cuidador, name='info_cuidador'),
    path('info/paciente', views.info_paciente, name='info_paciente'),
    path('info/paciente/registrar_evento',views.registrar_evento, name='registrar_evento'),
    path('info/registrar/', views.registrar_paciente, name='registrar_paciente'),
    path('info/editar_perfil_paciente/<int:id_paciente>/', views.editar_perfil_paciente, name='editar_perfil_paciente'),
    path('info/registro_perfil/', views.registrar_perfil_cuidador, name='registrar_perfil_cuidador'),
    path('info/editar_perfil/<int:id_cuidador>/', views.editar_perfil_cuidador, name='editar_perfil_cuidador'),
    path('info/sintomas/registrar/', views.registrar_sintoma, name='registrar_sintoma'),
    path('info/test/', views.info_test, name='info_test'),
    path('info/test-npi/', views.test_npi, name='test_npi'),
    path('info/test-zarit/', views.test_zarit, name='test_zarit'),
]