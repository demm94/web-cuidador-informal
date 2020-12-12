from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente, Historial
from .forms import PacienteForm, RegistroSintomaForm
from django.urls import reverse_lazy

# Create your views here.

@login_required # info_paciente requiere que el cuidador esté logeado en el sistema
def info_paciente(request):
    try:
        paciente = Paciente.objects.get(user=request.user)
    except Paciente.DoesNotExist:
        paciente = None
    historial = Historial.objects.filter(paciente=paciente)
    return render(request, 'patient/info_paciente.html', {'paciente': paciente, 'historial': historial})

@login_required # registrar_paciente requiere que el cuidador esté logeado en el sistema
def registrar_paciente(request):
    paciente = Paciente.objects.filter(user=request.user) 
    if not paciente:    #Evita que se vuelva a registrar un paciente si ya hay uno registrado, redireccionando a "Mi paciente"
        if request.method == 'POST':
            form = PacienteForm(request.POST)
            if form.is_valid():
                paciente = form.save(commit=False)
                paciente.user = request.user
                paciente.save()
                return redirect(reverse_lazy('info_paciente'))
        else:
            form = PacienteForm()
            return render(request, 'patient/registrar_paciente.html', {'form': form})
    else:
        return redirect(reverse_lazy('info_paciente'))

@login_required
def registrar_sintoma(request):
    if request.method == 'POST':
        form = RegistroSintomaForm(request.POST)
        if form.is_valid():
            historial = form.save(commit=False)
            historial.paciente = Paciente.objects.get(user=request.user)
            historial.save()
            form.save_m2m()
            return redirect(reverse_lazy('info_paciente'))
    else:
        form = RegistroSintomaForm()
        return render(request, 'patient/registrar_sintoma.html', {'form': form})