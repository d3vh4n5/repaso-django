from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    contexto = {
        'titulo' : 'Bienvenidos a la prueba de mi página web con django, ahora dinámica',
        'nombre_usuario' : 'Pepito Manzanero',
        
    }
    return render(request, 'index.html', contexto)



def listar_alumnos(request):
    alumnos = ["Carlos", "Maria", "Jose", "Daniela"]

    resultado = ""

    for alumno in alumnos:
        resultado += "<p><b>Nombre : </b>"+ alumno + "</p>"
    
    return HttpResponse(resultado)
    