# -*- coding: utf-8 -*-
from django import forms


class UploadFileForm(forms.Form):
    '''Clase de form para el upload'''
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class DenunciaForm(forms.Form):
    '''Clase de form para denuncias'''
    correo = forms.CharField(max_length=200, label="Correo Elecctronico")
    marca = forms.CharField(max_length=200)
    modelo = forms.CharField(max_length=200)
    aniomodelo = forms.CharField(max_length=200)
    tipo = forms.CharField(max_length=200)
    colores = forms.CharField(max_length=200)
    velocidades = forms.CharField(max_length=200)
    marcavelocidades = forms.CharField(max_length=200)
    modelovelocidades = forms.CharField(max_length=200)
