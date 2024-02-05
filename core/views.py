from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AgregarAlumno

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

def agregar_alumno(request):

    if request.method == "POST":
        form = AgregarAlumno(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data['nombre'])
            print(form.cleaned_data['apellido'])
            print(form.cleaned_data['edad'])
            # Insertamos en la DB el nuevo alumno
            return HttpResponseRedirect("lista_alumnos")

    else:
        form = AgregarAlumno()

    context = {
        'titulo' : "Agregar alumno",
        'form' : form
    }

    return render(request, 'pages/agregar_alumno.html', context)

def form_simple(request):
    if request.method == "POST":
        print(request.POST)

    return render(request, "pages/form_simple.html")
    