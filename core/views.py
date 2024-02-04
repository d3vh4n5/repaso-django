from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hola mundo")

def listar_alumnos(request):
    alumnos = ["Carlos", "Maria", "Jose", "Daniela"]

    resultado = ""

    for alumno in alumnos:
        resultado += "<p><b>Nombre : </b>"+ alumno + "</p>"
    
    return HttpResponse(resultado)
    