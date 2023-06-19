from django.shortcuts import render, redirect, get_object_or_404
from .models import Pregunta, Topico, Subtopico, Tema, DetalleTema
from patient.models import Evento,Cuidador, Test, RespuestaNPI, RespuestaZarit
from patient.forms import TestNPIForm, TestZaritForm
from content.forms import PreguntaForm, RespuestaForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Topico
from django.urls import reverse_lazy
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore


import datetime
import pandas as pd
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objs as go
import numpy as np



# Decorators

def check_medico(request):
    if request.is_medico and request.is_authenticated:
        return True
    else:
        return False
def pagination(list,request):
    paginator = Paginator(list,6)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un entero, mostrar la primera página
        content = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera del rango (por ejemplo, 9999), mostrar la última página de resultados
        content = paginator.page(paginator.num_pages)
    return content

def filtro_preguntas(rango_fechas, estado_respuesta,preguntas):
    if rango_fechas:
            fecha_min, fecha_max = rango_fechas.split(" - ")
            fecha_min = datetime.datetime.strptime(fecha_min, "%d/%m/%Y").date()
            fecha_max = datetime.datetime.strptime(fecha_max, "%d/%m/%Y").date()
            preguntas = preguntas.filter(fecha_creacion__range=[fecha_min, fecha_max])

    if estado_respuesta == "respondida":
            preguntas = preguntas.exclude(respuesta__isnull=True)
    elif estado_respuesta == "no_respondida":
            preguntas = preguntas.filter(respuesta__isnull=True)
    
    return preguntas
def chart_zarit(zarit):
    zarit_data = [
        {
            'Fecha': z.test.fecha,
            'Evaluacion': z.evaluacion,
            'Resultado': z.resultado,
        } for z in zarit
    ]

    df = pd.DataFrame(zarit_data)

    fig = px.scatter(
        df, x='Fecha',y='Resultado',color="Evaluacion", size = "Resultado",
        color_discrete_map={
            'Sobrecarga Intensa': 'red',
            'Sobrecarga Ligera': 'orange',
            'Ausencia de Sobrecarga': 'green',

        },
        category_orders={
            'Evaluacion': ['Sobrecarga Intensa', 'Sobrecarga Ligera', 'Ausencia de Sobrecarga'],
        }
    )
    fig.update_layout(title='Gráfico de Zarit', xaxis=dict(title='Fecha',tickformat='%d/%m/%Y'), yaxis=dict(title='Resultado'))
    return fig           
def chart_npi(npi):
    npi_data = {
        'Fecha': [r.test.fecha for r in npi],
    }
    for i in range(1, 13):
        npi_data[f'r{i}b'] = [getattr(r, f'r{i}b') if getattr(r, f'r{i}b') != 9 else -1 for r in npi]
    df = pd.DataFrame(npi_data)
    df.set_index('Fecha', inplace=True)
    columnas = [f'r{i}b' for i in range(1, 13)]
    fig2 = px.imshow(
        df[columnas].T, 
        labels=dict(y="Preguntas"),
        y=["Delirios", "Alucinaciones", "Agitación o Agresividad",
            "Depresión o disforia", "Ansiedad", "Euforia o exaltación",
            "Apatía o indiferencia", "Pérdida de la inhibición/Desinhibición",
            "Irritabilidad o labilidad", "Disturbio motor", "Conductas nocturnas",
            "Apetito y alimentación"],
        color_continuous_scale='Greens',
    )
    fig2.update_layout(
        title='Respuestas NPI',
        xaxis=dict(title='Fecha',tickformat='%d/%m/%Y'),
        coloraxis=dict(colorbar=dict(title='Severidad', thickness=25)),
        coloraxis_colorbar=dict(
            tickvals=[-1, 0, 1, 2, 3],
            ticktext=['No sabe', 'No cambia', 'Leve', 'Moderado', 'Severo'],
        )
    )
    return fig2
def chart_eventos(eventos):
    eventos_data = [
        {
            'Fecha': e.fecha,
            'Frecuencia de baño': e.f_baño,
            'Frecuencia de alimentación': e.f_alimentacion,
            'Horas de sueño': e.f_sueño,
            'Estado de ánimo': e.animo,
            'Otros':e.comentario
        } for e in eventos
    ]
    df = pd.DataFrame(eventos_data)

    fig3 = px.line(df, x='Fecha', 
                        y=[
                            'Estado de ánimo',
                            'Frecuencia de baño',
                            'Frecuencia de alimentación',
                            'Horas de sueño'
                        ],
                        markers=True,
                        hover_data={'Otros':True},
                        symbol="variable",
                    )
    fig3.update_layout(
                title='Eventos',
                xaxis=dict(title='Fecha',tickformat='%d/%m/%Y'),
                yaxis=dict(title='Valores')
            )
    fig3.update_traces(marker=dict(size=10))
    return fig3

@login_required
def home(request):
    busqueda = request.GET.get("buscar")
    cuidadores = Cuidador.objects.filter(medico__id = request.user.id)
    temas = None
    if busqueda:
        temas = Tema.objects.filter(
            Q(nombre__icontains = busqueda)
        ).distinct
    return render(request, 'content/home.html', {'cuidadores': cuidadores, 'temas': temas})

@login_required
def topicos(request):
    busqueda = request.GET.get("buscar")
    filtro_topico = request.GET.get("filtro_topico")

    topicos_list = Topico.objects.all()
    topicos = pagination(topicos_list,request)
    if busqueda:
        topicos = Topico.objects.filter(
            Q(nombre__icontains = busqueda)
        ).distinct
    if filtro_topico:
        topicos = topicos_list.filter(id=filtro_topico)
    
    return render(request, 'content/topicos.html', {'topicos': topicos, 'lista_topicos': topicos_list})

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
    subtopicos_list = Subtopico.objects.filter(topico__id = id_topico)
    subtopicos = pagination(subtopicos_list,request)
    if subtopicos_list:
        # return redirect('content/subtopicos/')
        # Muestra todos esos subtopicos para seleccionar
        return render(request, 'content/subtopicos.html', {'subtopicos': subtopicos, 'nombreAnterior': nombreTopico})
    else:
        
        temas_list = Tema.objects.filter(topico__id = id_topico)
        temas =pagination(temas_list,request)
        if temas_list:
            return render(request, 'content/temas.html', {'temas': temas, 'nombreAnterior': nombreTopico})
        else:
            detalles_list = DetalleTema.objects.filter(topico__id = id_topico)
            detalles = pagination(detalles_list,request)
        
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
    temas_list = Tema.objects.filter(nombre__icontains = "Consejos")
    temas = pagination(temas_list,request)
    
    return render(request, 'content/consejos.html', {'temas': temas})

@login_required
def test_screen(request):
    return render(request,'content/screenTest.html')


@login_required
@user_passes_test(check_medico, settings.LOGIN_REDIRECT_URL) 
def test_cuidador(request):
    
    id_usuario = request.session.get('session_cuidador')
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
def ver_zarit(request, id_zarit):
    form_instance = RespuestaZarit.objects.get(id=id_zarit)
    form = TestZaritForm(instance=form_instance)
    return render(request, 'content/testZarit.html', {'form': form, 'form_instance': form_instance})
@login_required
@user_passes_test(check_medico, settings.LOGIN_REDIRECT_URL) 
def agregar_cuidador(request):
    if request.method=='POST':
        id_cuidador = request.POST.get('id_cuidador')
        if id_cuidador:
            try:
                cuidador = Cuidador.objects.get(id=id_cuidador)
                cuidador.medico = request.user
                cuidador.save()
            except Cuidador.DoesNotExist:
                print("Cuidador no existe")
                
    cuidadores_list = Cuidador.objects.filter(medico__isnull=True)

    return render(request, 'content/agregarCuidador.html',{'cuidadores_list': cuidadores_list})
@login_required
@user_passes_test(check_medico, settings.LOGIN_REDIRECT_URL) 
def eliminar_cuidador(request,id_cuidador):
    cuidador = get_object_or_404(Cuidador, id=id_cuidador)
    cuidador.medico = None  # Establece la relación con el médico como nula
    cuidador.save()
    return redirect(reverse_lazy('home'))
@login_required
@user_passes_test(check_medico, settings.LOGIN_REDIRECT_URL) 
def perfil_cuidador(request, id_cuidador):

    try:
        cuidador = Cuidador.objects.get(user=id_cuidador)
        eventos = Evento.objects.filter(user = id_cuidador).order_by('-fecha')
    except Cuidador.DoesNotExist:
        cuidador = None

    if cuidador and cuidador.medico_id == request.user.id: 
        request.session['session_cuidador'] = id_cuidador
        return render(request ,'content/perfilCuidador.html',{'cuidador':cuidador,'eventos':eventos})
    else: 
        return redirect(reverse_lazy('home'))



@login_required
def preguntas(request,pregunta_id = None):
    if request.user.is_cuidador:
        form = PreguntaForm(request.POST or None)
        preguntas = Pregunta.objects.filter(user_creador = request.user).order_by('-fecha_creacion')
        busqueda = request.GET.get("buscar")
        
        estado_respuesta = request.GET.get("estado_respuesta")
        rango_fechas = request.GET.get("rango_fechas")
        preguntas = filtro_preguntas(rango_fechas,estado_respuesta,preguntas)
        if form.is_valid():
            pregunta = form.save(commit=False)
            pregunta.user_creador = request.user 
            pregunta.save()
            return redirect(reverse_lazy('preguntas'))
       
        preguntas = pagination(preguntas,request)

        if busqueda:
            preguntas = Pregunta.objects.filter(
                Q(pregunta__icontains = busqueda)
            ).distinct
        return render(request, 'content/preguntas.html',{'form':form, 'preguntas':preguntas})
    
    elif request.user.is_medico:
        if request.session.get('session_cuidador'):
            if pregunta_id != None:
                pregunta = Pregunta.objects.get(id=pregunta_id)
            id_cuidador = request.session.get('session_cuidador')
            cuidador = Cuidador.objects.get(user__id=id_cuidador)
            preguntas = Pregunta.objects.filter(user_creador = id_cuidador ).order_by('-fecha_creacion')
            form = RespuestaForm(request.POST or None)
            busqueda = request.GET.get("buscar")        
            
            estado_respuesta = request.GET.get("estado_respuesta")
            rango_fechas = request.GET.get("rango_fechas")
            preguntas = filtro_preguntas(rango_fechas,estado_respuesta,preguntas)        
            
            if form.is_valid():
                pregunta.respuesta = form.cleaned_data['respuesta']
                pregunta.user_responde = request.user 
                pregunta.save()
                return redirect(reverse_lazy('preguntas'))
                
            preguntas = pagination(preguntas,request)
            
            if busqueda:
                preguntas = Pregunta.objects.filter(
                    Q(pregunta__icontains = busqueda)
                ).distinct
            return render(request,'content/preguntas.html',{'form':form,'preguntas':preguntas, 'cuidador':cuidador})
        else: 
            return redirect(reverse_lazy('home'))
@login_required
@user_passes_test(check_medico, settings.LOGIN_REDIRECT_URL) 
def informe_grafico(request):
    
    if request.session.get('session_cuidador'):
        id_cuidador = request.session.get('session_cuidador')
        cuidador = Cuidador.objects.get(user__id=id_cuidador) 
        zarit = RespuestaZarit.objects.filter(test__cuidador__id = id_cuidador)
        npi = RespuestaNPI.objects.filter(test__cuidador__id = id_cuidador)
        eventos = Evento.objects.filter(user=id_cuidador).order_by('fecha')
        context = {'cuidador':cuidador}
        tipo_grafico = request.GET.get("tipo_grafico")

        if tipo_grafico == "" or not tipo_grafico:
            print(tipo_grafico)
            if zarit:
                fig = chart_zarit(zarit)
                zarit_plot = plot(fig,output_type ="div")
                context['zarit_plot'] = zarit_plot
        

            if npi:
                fig2 = chart_npi(npi)
                npi_plot = plot(fig2,output_type ="div")

                context['npi_plot'] = npi_plot

            if eventos:
                fig3 = chart_eventos(eventos)
                eventos_plot = plot(fig3,output_type ="div")
                context['eventos_plot'] = eventos_plot
        elif tipo_grafico == "ZARIT" and zarit:
            fig = chart_zarit(zarit)
            zarit_plot = plot(fig,output_type ="div")
            context['zarit_plot'] = zarit_plot
        elif tipo_grafico == "NPI" and npi:
            fig2 = chart_npi(npi)
            npi_plot = plot(fig2,output_type ="div")
            context['npi_plot'] = npi_plot
        elif tipo_grafico == "Eventos" and eventos:
            fig3 = chart_eventos(eventos)
            eventos_plot = plot(fig3,output_type ="div")
            context['eventos_plot'] = eventos_plot

        return render(request,'content/informeGrafico.html',context)