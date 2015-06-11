#!/usr/bin/python
# -*- coding: utf-8 -*-
__prj__ = 'BikeRobada'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'marcelo martinovic'
__email__ = 'marcelo.martinovic@gmail.com'
__url__ = ''
__date__ = '2014/08/11'

from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.template import RequestContext
from bicicletas.models import Denuncias
from django.core.context_processors import csrf
from django.db.models import Q
#from django.utils import simplejson
import json as simplejson
import socket
import smtplib
import datetime
import hashlib
from os import path
from django.http import *
from django.shortcuts import render_to_response
from forms import DenunciaForm
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)  # seconds
def contacto_index(request):
    '''Muestra pantalla de contacto'''
    titulo = "Contactarnos..."
    cantidad = Denuncias.objects.count()
    activos = Denuncias.objects.filter(activo=True).count()
    recuperados = Denuncias.objects.filter(activo=False).count()
    context = RequestContext(request,
                             {'cantidadDenuncias': cantidad,
                                 'activos': activos,
                                 'recuperados': recuperados,
                                 'titulo': titulo})
    return render(request, 'contacto/index.html', context)


@cache_page(60 * 15)  # seconds
def informacion(request):
    '''Muestra la pantalla de informacion'''
    return render(request, 'informacion.html')


@cache_page(60 * 15)  # seconds
def consejos_index(request):
    '''Muestra la pantalla de consejos'''
    titulo = "Consejos para no ser victima"
    cantidad = Denuncias.objects.count()
    activos = Denuncias.objects.filter(activo=True).count()
    recuperados = Denuncias.objects.filter(activo=False).count()
    context = RequestContext(request,
                             {'cantidadDenuncias': cantidad,
                                 'activos': activos,
                                 'recuperados': recuperados,
                                 'titulo': titulo})
    return render(request, 'consejos/index.html', context)


def testForms(request):
    '''Este metodo es solo para pruebas'''
    if request.method == "GET":
        form = DenunciaForm()
    else:
        form = DenunciaForm(request.POST)

    return render(request, 'denuncias/test.html', {"form": form, })


################################################################
# #  Recupero
def recuperada_index(request):
    ''''''
    titulo = "Avisar de un recupero"
    cantidad = Denuncias.objects.count()
    activos = Denuncias.objects.filter(activo=True).count()
    recuperados = Denuncias.objects.filter(activo=False).count()
    context = RequestContext(request,
                             {'cantidadDenuncias': cantidad,
                                 'activos': activos,
                                 'recuperados': recuperados,
                                 'titulo': titulo})
    return render(request, 'recuperada/index.html', context)


def aviso_recuperada(request):
    '''Envia el aviso de recupero'''

    titulo = "Avisar de un recupero"
    cantidad = Denuncias.objects.count()
    activos = Denuncias.objects.filter(activo=True).count()
    recuperados = Denuncias.objects.filter(activo=False).count()

    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        correo = request.POST["correo"]
        if len(correo) > 10:
            fecha = datetime.datetime.strftime(datetime.datetime.now(),
                                               "%Y%m%d")
            m = hashlib.md5()
            m.update(correo + fecha)
            hashCheck = m.hexdigest()
            print(hashCheck)
            msg = "Hola.\n"
            msg += "Este correo llega por solicitud a la pagina ...\n"
            msg += "Haciendo click en la URL enviada daras terminado el evento\n"
            msg += "denunciado sea por que has podido recuperar "
            msg += "tu bicicleta de manera"
            msg += "total o parcial o has decidido abandonar la busqueda.\n"
            msg += "No seran enviado ningun tipo mail desde el "
            msg += "sistema luego de esto.\n"
            msg += "Codigo para terminar el evento \n\n"
            msg += "\t'http://bikerobada.no-ip.info:8000/recuperada/baja/"
            msg += ("%s/%s\n\n'" % (correo, hashCheck))
            msg += "Gracias por usar el servicio, esperamos verte"
            msg += "en pronto rodando nuevamente."
            print(msg)
            from_addr = "marcelo.martinovic@gmail.com"
            to_addrs = correo.strip()
            # msg += "Codigo para terminar el evento 'http://dotworld.no-ip.info'"

            username = 'marcelo.martinovic'
            password = 'python2013'
            # The actual mail send
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(username, password)
            server.sendmail(from_addr, to_addrs, msg)
            server.quit()

    context = RequestContext(request,
                             {'avisoEmitido': cantidad,
                                 'activos': activos,
                                 'recuperados': recuperados,
                                 'titulo': titulo,
                                 'correo': correo,
                                 'avisoEmitido': True})
    if request.POST["fromPagina"] == "pagina":
        return render(request, 'recuperada/aviso_recuperada.html', context)
    else:
        return render(request, 'index.html', context)


def baja_recuperada(request, correo, verificacion):
    ''''''
    titulo = "Confirmacion de baja"
    cantidad = Denuncias.objects.count()
    activos = Denuncias.objects.filter(activo=True).count()
    recuperados = Denuncias.objects.filter(activo=False).count()
    fecha = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d")
    m = hashlib.md5()
    m.update(correo + fecha)
    hashCheck = m.hexdigest()
    if hashCheck != verificacion:
        correo = ""
    context = RequestContext(request,
                             {'cantidadDenuncias': cantidad,
                                 'activos': activos,
                                 'recuperados': recuperados,
                                 'titulo': titulo,
                                 'correo': correo})

    return render(request, 'recuperada/confirma_recuperada.html', context)


################################################################
# #  Denuncias

def index(request):
    '''Vista principal'''
    titulo = "Denuncias"
    cantidad = Denuncias.objects.count()
    activos = Denuncias.objects.filter(activo=True).count()
    recuperados = Denuncias.objects.filter(activo=False).count()
    context = RequestContext(request,
                             {'cantidadDenuncias': cantidad,
                                 'activos': activos,
                                 'recuperados': recuperados,
                                 'titulo': titulo})
    return render(request, 'denuncias/index.html', context)


def save_denuncias(request):
    '''Graba los datos'''
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        correo = request.POST['correo']
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        anioModelo = request.POST['anioModelo']
        tipo = request.POST['tipo']
        colores = request.POST['colores']
        velocidades = request.POST['velocidades']
        marcaVelocidades = request.POST['marcaVelocidades']
        modeloVelocidades = request.POST['modeloVelocidades']
        nroCuadro = request.POST['nroCuadro']
        nroHorquilla = request.POST['nroHorquilla']
        fechaRobo = request.POST['fechaRobo']
        lugarRobo = request.POST['lugarRobo']
        lugarDenuncia = request.POST['lugarDenuncia']
        telefonoContacto = request.POST['telefonoContacto']
        accesorios = request.POST['accesorios']
        detalle = request.POST['detalle']
        recompensa = request.POST['recompensa']
        condicion = request.POST['condicion']

        ##########################
        # # Verifica
        email = request.POST["correo"]
        cuadro = request.POST["nroCuadro"]
        horquilla = request.POST["nroHorquilla"]
        lista = Denuncias.objects.filter(
            Q(correo__contains=email) |
            Q(nrocuadro__contains=cuadro) |
            Q(nrohorquilla__contains=horquilla)).filter(activo=True)
        cantidad = lista.count()
        if cantidad >= 1:
            msg = 'Ha ocurrido un error, el email, numero de cuadro o \n'
            msg += 'numero de horquilla ya existe, '
            msg += 'por favor verifique o busque\n'
            msg += 'quien ha realizado la denuncia.\n'
            msg += 'No se grabar tu denuncia.'
            context = {'message': msg, 'boton_regreso': True}

            return render(request,
                'denuncias/mensaje_termino.html',
                context)
        else:
            pathPic = "pic_folder/None/nophoto.gif"

            print(request.FILES.items())
            #if len(request.FILES.items()) >= 1:
                #for key, file in request.FILES.items():
                    #pathPic = "pic_folder/%s" % file.name
                    #route = path.abspath(path.join(path.dirname('.'), 'static'))
                    #dest = open(route + path, 'w')
                    #if file.multiple_chunks:
                        #for c in file.chunks():
                            #dest.write(c)
                    #else:
                        #dest.write(file.read())
                    #dest.close()

            cs = Denuncias(
                correo=correo,
                marca=marca.upper(),
                modelo=modelo.upper(),
                aniomodelo=anioModelo,
                tipo=tipo,
                colores=colores.upper(),
                velocidades=velocidades,
                marcavelocidades=marcaVelocidades.upper(),
                modelovelocidades=modeloVelocidades.upper(),
                nrocuadro=nroCuadro,
                nrohorquilla=nroHorquilla,
                fecharobo=fechaRobo,
                lugarrobo=lugarRobo.upper(),
                lugardenuncia=lugarDenuncia.upper(),
                telefonocontacto=telefonoContacto,
                accesorios=accesorios.upper(),
                detalle=detalle.upper(),
                recompensa=recompensa,
                condicion=condicion,
                activo=True,
                foto=pathPic
            )
            cs.save()

            try:
                context = {'message':
                    'Tu denuncia ha sido registrada de manera exitosa.'}
            except:
                context = {'message':
                'Ha ocurrido un error y no se ha podido grabar tu denuncia.'}

            return render(request,
                'denuncias/mensaje_termino.html',
                context)


def handle_uploaded_file(f, nombre="none"):
    ''''''
    print("Nombre: %s" % nombre)
    with open('/home/marcelo/python/bikeRobada/file.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def comfirma_denuncias(response):
    '''Confirma accion de grabado'''
    pass


#########################################################################
# Busquedas
def busquedas_index(request):
    ''''''
    titulo = "Lista de robos"
    cantidad = Denuncias.objects.count()
    activos = Denuncias.objects.filter(activo=True).count()
    recuperados = Denuncias.objects.filter(activo=False).count()
    lista = Denuncias.objects.order_by('-fecharobo', 'marca', 'modelo').all()
    context = RequestContext(request,
                             {'lista': lista,
                                 'cantidadDenuncias': cantidad,
                                 'activos': activos,
                                 'recuperados': recuperados,
                                 'titulo': titulo})
    return render(request, 'busquedas/index.html', context)


def append_denuncias(request):
    '''Append to denuncia'''
    titulo = "Alta de denuncia"
    lectura = ""
    c = {}
    c.update(csrf(request))
    context = {"lectura": lectura, 'titulo': titulo}
    return render(request, 'denuncias/append_denuncias.html', context)


def view_denuncia(request):
    '''view denuncia'''
    titulo = "Consulta de denuncia"
    lectura = ""
    c = {}
    c.update(csrf(request))
    context = {}
    print(request.POST['q'])
    try:
        datos = get_list_or_404(Denuncias,
                              id=request.POST['q'])
        context = {"lectura": lectura, 'titulo': titulo, 'posts': datos}
        print(datos)
    except:
        pass

    return render(request, 'busquedas/busquedas_view.html', context)


def viewEvent(request):
    '''Ver el evento'''
    c = {}
    c.update(csrf(request))
    print(request.POST['q'].upper())
    q = request.POST['q'].upper()
    titulo = "Lista de robos"
    cantidad = Denuncias.objects.count()
    activos = Denuncias.objects.filter(activo=True).count()
    recuperados = Denuncias.objects.filter(activo=False).count()
    lista = Denuncias.objects.order_by('-fecharobo', 'marca', 'modelo').filter(
            Q(marca__contains=q) |
            Q(modelo__contains=q) |
            Q(nrocuadro__contains=q) |
            Q(nrohorquilla__contains=q) |
            Q(tipo__contains=q))
    context = RequestContext(request,
                             {'lista': lista,
                                 'cantidadDenuncias': cantidad,
                                 'activos': activos,
                                 'recuperados': recuperados,
                                 'titulo': titulo})
    return render(request, 'busquedas/index.html', context)



