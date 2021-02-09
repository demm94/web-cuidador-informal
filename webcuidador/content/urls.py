from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topicos/', views.topicos, name='topicos'),
    path('topicos/<int:id_topico>/infografia/', views.infografia, name='infografia'),
    path('consejos/<int:id_tema>/infografia/', views.infografia_consejos, name='infografia_consejos'),
    path('consejos/', views.consejos, name='consejos'),
    #path('secciones/topicos/<int:id_seccion>/', views.topicos, name='topicos'),
    #path('secciones/subtopicos/<int:id_topico>/', views.subtopicos, name='subtopicos'),
    path('consejos/contr1/<int:id_topico>/', views.top_controlador, name='top_controlador'),
    path('consejos/contr2/<int:id_subtopico>/', views.subtop_controlador, name='subtop_controlador'),
    path('consejos/contr3/<int:id_tema>/', views.tema_controlador, name='tema_controlador'),
    path('tests/<int:id_usuario>/', views.test_cuidador, name='test_cuidador'),
    path('tests/npi/<int:id_npi>/', views.ver_npi, name='ver_npi'),
    path('tests/zarit/<int:id_zarit>/', views.ver_zarit, name='ver_zarit'),
]