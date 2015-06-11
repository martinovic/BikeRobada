#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import RequestContext
from bicicletas.models import Denuncias
from django.core.context_processors import csrf


def home(request):
    '''Vista principal'''
    titulo = "Denuncias"
    cantidad = Denuncias.objects.count()
    activos = Denuncias.objects.filter(activo=True).count()
    recuperados = Denuncias.objects.filter(activo=False).count()
    print("ppal > %s" % cantidad)
    context = RequestContext(request,
                             {'cantidadDenuncias': cantidad,
                                 'activos': activos,
                                 'recuperados': recuperados,
                                 'titulo': titulo})
    return render(request, 'index.html', context)
