#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import RequestContext


def index(request):
    ''''''
    titulo = "Participan del proyecto"
    context = RequestContext(request,
                             {'titulo': titulo})
    return render(request, 'participantes/index.html', context)