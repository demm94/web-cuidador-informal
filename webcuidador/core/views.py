from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.

def portada(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('home'))
    return render(request, 'core/portada.html')

def inicio(request):
    return render(request, 'core/inicio.html')

def prueba(request):
    return render(request, 'core/prueba.html')

