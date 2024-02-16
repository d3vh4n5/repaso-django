from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import AgregarAlumno, RegistrarUsuarioForm
from core.models import Alumno
from datetime import date
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    contexto = {
        'titulo' : 'Bienvenidos a la prueba de mi página web con django, ahora dinámica',
        'nombre_usuario' : 'Pepito Manzanero',
        
    }
    return render(request, 'index.html', contexto)

def my_login(request):
    if request.method == "POST":
        #AuthenticationForm can also be used
        username= request.POST["username"]
        password = request.POST["password"]
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("User validated")
            print(user)
            form = login(request, user)
            messages.success(request, f"Bienvenido/a {username}")
            return redirect("index")
        else:
            print("User not validated")
            messages.error(request, f"Cuenta o contraseña incorrectos")
    
    form = AuthenticationForm()


    context = {
        'form' : form,
        'title' : 'Login'
    }
    return render(request, 'pages/login.html', context)

def my_logout(request):
    logout(request)
    return redirect('index')

def user_register(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado correctamente.")
            return render(request, 'pages/register.html')
            # return redirect('my_login')
    else:
        form = RegistrarUsuarioForm()
    
    context = {
        'form' : form,
        'title' : 'Login'
    }
    
    return render(request, 'pages/register.html', context)


def listar_alumnos(request):
    # alumnos = Alumno.objects.select_related('curso').all()
    # alumnos = Alumno.objects.values()
    alumnos = Alumno.objects.all()
    context = {
        'titulo': 'Listado de alumnos',
        'alumnos': alumnos
    }
    
    return render(request, 'pages/lista_alumnos.html', context)

@login_required
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
                # edad = form.cleaned_data['edad'],
                activo = form.cleaned_data['activo'],
                # turno = form.cleaned_data['turno'],
                # curso = form.cleaned_data['curso'],
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
    