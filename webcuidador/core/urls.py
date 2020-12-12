from django.urls import path
from . import views

urlpatterns = [
    path('', views.portada, name='portada'),
    path('prueba/', views.prueba, name='prueba'),
]