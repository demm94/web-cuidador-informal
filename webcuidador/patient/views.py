from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Evento, Paciente, Historial, Test, TipoTest, Cuidador
from .forms import RegistroEventoForm, PacienteForm, RegistroSintomaForm, TestNPIForm, TestZaritForm, RespuestaZarit, RespuestaNPI, CuidadorForm
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test

# Decorators 

def check_cuidador(request):
    if request.is_cuidador and request.is_authenticated:
        return True
    else:
        return False
        
# Create your views here.

@login_required # info_cuidador requiere que el cuidador esté logeado en el sistema
@user_passes_test(check_cuidador, settings.LOGIN_REDIRECT_URL) 
def info_cuidador(request):
    try:
        cuidador = Cuidador.objects.get(user=request.user)
        
    except Cuidador.DoesNotExist:
        cuidador = None
    return render(request, 'patient/info_cuidador.html', {'cuidador': cuidador})

@login_required # info_cuidador requiere que el cuidador esté logeado en el sistema
@user_passes_test(check_cuidador, settings.LOGIN_REDIRECT_URL) 
def info_test(request):
    test = Test.objects.filter(cuidador=request.user)

    return render(request,'patient/info_test.html', {'test': test})

@login_required # info_cuidador requiere que el cuidador esté logeado en el sistema
@user_passes_test(check_cuidador, settings.LOGIN_REDIRECT_URL) 
def info_paciente(request):
    try:
        paciente = Paciente.objects.get(user = request.user)
        eventos = Evento.objects.filter(user=request.user).order_by('-fecha')
        form = RegistroEventoForm(request.POST)

    except Paciente.DoesNotExist:
        paciente = None

    if paciente:
        return render(request,'patient/info_paciente.html',{'paciente': paciente,'eventos': eventos,'form': form})
    else:
        return redirect(reverse_lazy('registrar_paciente'))



@login_required # registrar_paciente requiere que el cuidador esté logeado en el sistema
@user_passes_test(check_cuidador, settings.LOGIN_REDIRECT_URL) 
def registrar_paciente(request):
    paciente = Paciente.objects.filter(user=request.user) 
    if not paciente:    #Evita que se vuelva a registrar un paciente si ya hay uno registrado, redireccionando a "Mi paciente"
        if request.method == 'POST':
            form = PacienteForm(request.POST)
            if form.is_valid():
                paciente = form.save(commit=False)
                paciente.user = request.user
                paciente.save()
                return redirect(reverse_lazy('info_cuidador'))
        else:
            form = PacienteForm()
            return render(request, 'patient/registrar_paciente.html', {'form': form})
    else:
        return redirect(reverse_lazy('info_cuidador'))
    
@login_required 
@user_passes_test(check_cuidador, settings.LOGIN_REDIRECT_URL)
def editar_perfil_paciente(request, id_paciente):
    paciente = Paciente.objects.get(user=request.user) 
    #Evita que se vuelva a ingresar el perfil del cuidador si ya hay uno registrado, redireccionando a "Mi paciente"
    #además evita ingresar a editar otro "cuidador" desde la URL 
    if paciente and id_paciente==paciente.id:    
        if request.method == 'POST':
            form_instance = Paciente.objects.get(pk=id_paciente)
            form = PacienteForm(request.POST, instance=form_instance)
            if form.is_valid():
                print("Valido")
                form.save()
                return redirect(reverse_lazy('info_paciente') + '?edit')
        else:
            # Mostrar datos de perfil ya creado en el formulario
            form_instance = Paciente.objects.get(pk=id_paciente)
            form = PacienteForm(instance=form_instance)
            return render(request, 'patient/editar_perfil_paciente.html', {'form': form, 'form_instance': form_instance})
    else:
        print("No valido")
        return redirect(reverse_lazy('info_paciente'))
@login_required
@user_passes_test(check_cuidador, settings.LOGIN_REDIRECT_URL)
def registrar_evento(request):
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.user = request.user
            evento.save()
            return redirect(reverse_lazy('info_paciente'))
    else:
        form = RegistroEventoForm()
        return render(request, 'patient/registrar_evento.html', {'form': form})


@login_required
@user_passes_test(check_cuidador, settings.LOGIN_REDIRECT_URL)
def registrar_sintoma(request):
    if request.method == 'POST':
        form = RegistroSintomaForm(request.POST)
        if form.is_valid():
            historial = form.save(commit=False)
            historial.paciente = Paciente.objects.get(user=request.user)
            historial.save()
            form.save_m2m()
            return redirect(reverse_lazy('info_cuidador'))
    else:
        form = RegistroSintomaForm()
        return render(request, 'patient/registrar_sintoma.html', {'form': form})

@login_required
@user_passes_test(check_cuidador, settings.LOGIN_REDIRECT_URL)
def test_npi(request):
    cuidador = Cuidador.objects.filter(user=request.user)
    if cuidador:
        if request.method == 'POST':
            form = TestNPIForm(request.POST)
            if form.is_valid():
                # Se crea el objeto test
                tipo_test = TipoTest.objects.get(nombre="NPI")
                if tipo_test:
                    test = Test(tipo_test=tipo_test, cuidador=request.user)
                    test.save()
                NPI = form.save(commit=False)
                NPI.test = test
                NPI.save()
                return redirect(reverse_lazy('info_cuidador') + '?npi')
        else:
            #form_instance = RespuestaNPI.objects.get(test__id=8)
            #form = TestNPIForm(instance=form_instance)
            form = TestNPIForm()
        return render(request, 'patient/testNPI.html', {'form': form})
    else:
        return redirect(reverse_lazy(settings.LOGIN_REDIRECT_URL) + '?profile_error')

@login_required
@user_passes_test(check_cuidador, settings.LOGIN_REDIRECT_URL)
def test_zarit(request):
    cuidador = Cuidador.objects.filter(user=request.user)
    if cuidador:
        if request.method == 'POST':
            form = TestZaritForm(request.POST)
            if form.is_valid():
                resultado = 0
                evaluacion = ''
                for key, value in form.cleaned_data.items():
                    resultado+=int(value)
                if resultado <= 46:
                    evaluacion = "Ausencia de Sobrecarga"
                elif 47 <= resultado <= 55:
                    evaluacion = "Sobrecarga Ligera"
                else:
                    evaluacion = "Sobrecarga Intensa"

                #Se crea el objeto test
                tipo_test = TipoTest.objects.get(nombre="ZARIT")

                if tipo_test:
                    test = Test(tipo_test=tipo_test, cuidador=request.user)
                    test.save()
                ZARIT = form.save(commit=False)
                ZARIT.test = test
                ZARIT.resultado = resultado
                ZARIT.evaluacion = evaluacion
                ZARIT.save()
                return redirect(reverse_lazy('info_cuidador') + '?zarit')
        else:
            form = TestZaritForm()
        return render(request, 'patient/testZarit.html', {'form': form})
    else:
        return redirect(reverse_lazy(settings.LOGIN_REDIRECT_URL) + '?profile_error')

@login_required # registrar perfil de cuidador requiere que el cuidador esté logeado en el sistema
@user_passes_test(check_cuidador, settings.LOGIN_REDIRECT_URL)
def registrar_perfil_cuidador(request):
    cuidador = Cuidador.objects.filter(user=request.user) 
    if not cuidador:    #Evita que se vuelva a ingresar el perfil del cuidador si ya hay uno registrado, redireccionando a "Mi paciente"
        if request.method == 'POST':
            form = CuidadorForm(request.POST)
            if form.is_valid():
                paciente = form.save(commit=False)
                paciente.user = request.user
                paciente.save()
                return redirect(reverse_lazy('info_cuidador')+ '?create')
        else:
            form = CuidadorForm()
            return render(request, 'patient/registro_perfil_cuidador.html', {'form': form})
    else:
        return redirect(reverse_lazy('info_cuidador'))

@login_required # registrar perfil de cuidador requiere que el cuidador esté logeado en el sistema
@user_passes_test(check_cuidador, settings.LOGIN_REDIRECT_URL)
def editar_perfil_cuidador(request, id_cuidador):
    cuidador = Cuidador.objects.get(user=request.user) 
    #Evita que se vuelva a ingresar el perfil del cuidador si ya hay uno registrado, redireccionando a "Mi paciente"
    #además evita ingresar a editar otro "cuidador" desde la URL 
    if cuidador and id_cuidador==cuidador.id:    
        if request.method == 'POST':
            form_instance = Cuidador.objects.get(pk=id_cuidador)
            form = CuidadorForm(request.POST, instance=form_instance)
            if form.is_valid():
                print("Valido")
                form.save()
                return redirect(reverse_lazy('info_cuidador') + '?edit')
        else:
            # Mostrar datos de perfil ya creado en el formulario
            form_instance = Cuidador.objects.get(pk=id_cuidador)
            form = CuidadorForm(instance=form_instance)
            return render(request, 'patient/editar_perfil_cuidador.html', {'form': form, 'form_instance': form_instance})
    else:
        print("No valido")
        return redirect(reverse_lazy('info_cuidador'))