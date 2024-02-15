from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import AgregarAlumno
from core.models import Alumno
from datetime import date

# Create your views here.
def index(request):
    contexto = {
        'titulo' : 'Bienvenidos a la prueba de mi página web con django, ahora dinámica',
        'nombre_usuario' : 'Pepito Manzanero',
        
    }
    return render(request, 'index.html', contexto)



def listar_alumnos(request):
    alumnos = Alumno.objects.select_related('curso').all()
    # alumnos = Alumno.objects.values()
    # alumnos = Alumno.objects.all()
    context = {
        'titulo': 'Listado de alumnos',
        'alumnos': alumnos
    }
    
    return render(request, 'pages/lista_alumnos.html', context)

def agregar_alumno(request):

    if request.method == "POST":
        form = AgregarAlumno(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data['nombre'])
            print(form.cleaned_data['apellido'])
            print(form.cleaned_data['edad'])
            print(form.cleaned_data['fecha_alta'])
            # Insertamos en la DB el nuevo alumno

            alumno = Alumno(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                dni = form.cleaned_data['dni'],
                edad = form.cleaned_data['edad'],
                activo = form.cleaned_data['activo'],
                turno = form.cleaned_data['turno'],
                curso = form.cleaned_data['curso'],
                sexo = form.cleaned_data['sexo'],
                fecha_ingreso = form.cleaned_data['fecha_alta']
            )

            alumno.save()

            return HttpResponseRedirect(reverse("listar_alumnos"))

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
    