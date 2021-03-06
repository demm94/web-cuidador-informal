from django.shortcuts import render, redirect
from .models import Topico, Subtopico, Tema, DetalleTema
from patient.models import Cuidador, Test, RespuestaNPI, RespuestaZarit
from patient.forms import TestNPIForm, TestZaritForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Topico
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings

# Decorators

def check_medico(request):
    if request.is_medico and request.is_authenticated:
        return True
    else:
        return False

@login_required
def home(request):
    busqueda = request.GET.get("buscar")
    cuidadores = Cuidador.objects.all()
    temas = None
    if busqueda:
        print("Holaa jeje")
        temas = Tema.objects.filter(
            Q(nombre__icontains = busqueda)
        ).distinct
    return render(request, 'content/home.html', {'cuidadores': cuidadores, 'temas': temas})

@login_required
def topicos(request):
    busqueda = request.GET.get("buscar")
    topicos = Topico.objects.all()
    dataSerialize = serializers.serialize('json', topicos, fields=['nombre'])
    if busqueda:
        print("Holaaa")
        topicos = Topico.objects.filter(
            Q(nombre__icontains = busqueda)
        ).distinct
    return render(request, 'content/topicos.html', {'topicos': topicos, 'data': dataSerialize})

@login_required
def infografia(request, id_topico):
    topico = Topico.objects.get(id = id_topico)
    return render(request, 'content/infografia.html', {'topico': topico})

@login_required
def infografia_consejos(request, id_tema):
    tema = Tema.objects.get(id = id_tema)
    return render(request, 'content/infografia.html', {'tema': tema})

@login_required
def top_controlador(request, id_topico):
    nombreTopico = Topico.objects.get(id = id_topico) # Link anterior
    subtopicos = Subtopico.objects.filter(topico__id = id_topico)
    # Si existen subtopicos asociados a ese id_topico
    if subtopicos:
        # return redirect('content/subtopicos/')
        # Muestra todos esos subtopicos para seleccionar
        return render(request, 'content/subtopicos.html', {'subtopicos': subtopicos, 'nombreAnterior': nombreTopico})
    else:
        temas = Tema.objects.filter(topico__id = id_topico)
        if temas:
            return render(request, 'content/temas.html', {'temas': temas, 'nombreAnterior': nombreTopico})
        else:
            detalles = DetalleTema.objects.filter(topico__id = id_topico)
            return render(request, 'content/detalles.html', {'detalles': detalles, 'nombreAnterior': nombreTopico})

@login_required
def subtop_controlador(request, id_subtopico):
    nombreSubtopico = Subtopico.objects.get(id = id_subtopico) # Link anterior
    temas = Tema.objects.filter(subtopico__id = id_subtopico)
    if temas:
        return render(request, 'content/temas.html', {'temas': temas, 'nombreAnterior': nombreSubtopico})
    else:
        detalles = DetalleTema.objects.filter(subtopico__id = id_subtopico)
        return render(request, 'content/detalles.html', {'detalles': detalles, 'nombreAnterior': nombreSubtopico})

@login_required
def tema_controlador(request, id_tema):
    nombreTema = Tema.objects.get(id = id_tema)
    detalles = DetalleTema.objects.filter(tema__id = id_tema)
    if detalles:
        return render(request, 'content/detalles.html', {'detalles': detalles, 'nombreAnterior': nombreTema})

@login_required
def consejos(request):
    temas = Tema.objects.filter(nombre__icontains = "Consejos")
    return render(request, 'content/consejos.html', {'temas': temas})

@login_required
@user_passes_test(check_medico, settings.LOGIN_REDIRECT_URL) 
def test_cuidador(request, id_usuario):
    cuidador = Cuidador.objects.get(user__id=id_usuario)
    zarit = RespuestaZarit.objects.filter(test__cuidador__id = id_usuario)
    npi = RespuestaNPI.objects.filter(test__cuidador__id = id_usuario)
    return render(request, 'content/tests.html', {'zarit': zarit, 'npi': npi, 'cuidador': cuidador})

@login_required
@user_passes_test(check_medico, settings.LOGIN_REDIRECT_URL) 
def ver_npi(request, id_npi):
    form_instance = RespuestaNPI.objects.get(id=id_npi)
    form = TestNPIForm(instance=form_instance)
    return render(request, 'content/testNPI.html', {'form': form, 'form_instance': form_instance})

@login_required
@user_passes_test(check_medico, settings.LOGIN_REDIRECT_URL) 
def ver_zarit(request, id_zarit):
    form_instance = RespuestaZarit.objects.get(id=id_zarit)
    form = TestZaritForm(instance=form_instance)
    return render(request, 'content/testZarit.html', {'form': form, 'form_instance': form_instance})

