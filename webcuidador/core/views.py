from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.

def portada(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('home'))
    return render(request, 'core/portada.html')

