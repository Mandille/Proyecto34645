from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.

def curso(request):

    curso1= Curso(nombre="JavaScript",comision=34645)
    curso1.save()
    cadena_texto=f"curso guardado: Nombre: {curso1.nombre}, comision: {curso1.comision}"
    return HttpResponse(cadena_texto)

 def cursos(request):
    return HttpResponse ("Esto es una vista de cursos")

 def estudiantes(request):
    return HttpResponse ("Esto es una vista de estudiantes")

 def profesores(request):
    return HttpResponse ("Esto es una vista de profesores")

 def entregables(request):
    return HttpResponse ("Esto es una vista de entregables")

 def inicio(request):
    return HttpResponse ("Estoy en inicio!")

