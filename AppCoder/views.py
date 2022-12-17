from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.

def curso(request):

    curso1= Curso(nombre="JavaScript",comision=34645)
    curso1.save()
    cadena_texto=f"curso guardado: Nombre: {curso1.nombre}, comision: {curso1.comision}"
    return HttpResponse(cadena_texto)