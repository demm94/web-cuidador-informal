from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topicos/', views.topicos, name='topicos'),
    path('consejos/', views.consejos, name='consejos'),
    #path('secciones/topicos/<int:id_seccion>/', views.topicos, name='topicos'),
    #path('secciones/subtopicos/<int:id_topico>/', views.subtopicos, name='subtopicos'),
    path('controlador1/<int:id_topico>/', views.top_controlador, name='top_controlador'),
    path('controlador2/<int:id_subtopico>/', views.subtop_controlador, name='subtop_controlador'),
    path('controlador3/<int:id_tema>/', views.tema_controlador, name='tema_controlador'),
]