from django.shortcuts import render, redirect
from .models import Topico, Subtopico, Tema, DetalleTema
from patient.models import Paciente
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Topico
from django.urls import reverse
from django.core import serializers

@login_required
def home(request):
    pacientes = Paciente.objects.all()
    '''busqueda = request.GET.get("buscar")
    #secciones = Seccion.objects.all()

    if busqueda and request.user.is_medico:
        #pacientes = Paciente.objects.filter(
            #Q(nombres__icontains = busqueda) |
            #Q(apellidos__icontains = busqueda) |
            #Q(edad__icontains = busqueda) |
            #Q(estado_civil__icontains = busqueda)
        #).distinct
    elif busqueda and request.user.is_medico == False:
        #secciones = Seccion.objects.filter(
            #Q(nombre__icontains = busqueda) |
            #Q(descripcion__icontains = busqueda)
        #).distinct'''
    return render(request, 'content/secciones.html', {'pacientes': pacientes})

'''def topicos(request, id_seccion):
    #seccion = Seccion.objects.get(id=id_seccion)
    return render(request, 'content/topicos.html', {'seccion': seccion})

def subtopicos(request, id_topico):
    subtopicos = Subtopico.objects.filter(topico=id_topico)
    print(subtopicos)
    return render(request, 'content/subtopicos.html', {'subtopicos': subtopicos})'''

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

def infografia(request, id_topico):
    topico = Topico.objects.get(id = id_topico)
    return render(request, 'content/infografia.html', {'topico': topico})

#def subtopicos(request, id_topico):
    # Todos los subtopicos asociados a id_topico
    #subtopicos = Subtopico.objects.filter(topico__id = id_topico)

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

    #subtopicos = Subtopico.objects.filter(topico__id = id_topico)
    #url = '{}'.format(reverse('topicos'))
    #print(url)
    #return redirect(url)
    #return render(request, 'content/subtopicos.html', {'subtopicos': subtopicos})

@login_required
def consejos(request):
    temas = Tema.objects.filter(nombre__icontains = "Consejos")
    return render(request, 'content/consejos.html', {'temas': temas})
