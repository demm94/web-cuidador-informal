from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('eliminar_cuidador/<int:id_cuidador>', views.eliminar_cuidador,name='eliminar_cuidador'),
    path('preguntas/', views.preguntas, name='preguntas' ),
    path('preguntas/<int:pregunta_id>/', views.preguntas ,name='responder_pregunta'),
    path('topicos/', views.topicos, name='topicos'),
    path('topicos/<int:id_topico>/infografia/', views.infografia, name='infografia'),
    path('consejos/<int:id_tema>/infografia/', views.infografia_consejos, name='infografia_consejos'),
    path('consejos/', views.consejos, name='consejos'),
    path('consejos/contr1/<int:id_topico>/', views.top_controlador, name='top_controlador'),
    path('consejos/contr2/<int:id_subtopico>/', views.subtop_controlador, name='subtop_controlador'),
    path('consejos/contr3/<int:id_tema>/', views.tema_controlador, name='tema_controlador'),
    path('tests/',views.test_screen, name = 'test_screen'),
    path('tests_cuidador/', views.test_cuidador, name='test_cuidador'),
    path('tests/npi/<int:id_npi>/', views.ver_npi, name='ver_npi'),
    path('tests/zarit/<int:id_zarit>/', views.ver_zarit, name='ver_zarit'),
    path('agregar_cuidador/', views.agregar_cuidador, name='agregar_cuidador'),
    path('perfil_cuidador/<int:id_cuidador>/', views.perfil_cuidador, name='perfil_cuidador'),
]