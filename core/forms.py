from django import forms
from .models import *

class AgregarAlumno(forms.Form):

    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche"),
    )

    SEXO_CHOICES = (
        ('O', 'Otro'),
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    nombre = forms.CharField(label="Nombre", max_length=20, min_length=3)
    apellido = forms.CharField(label="Apellido", max_length=20, min_length=2)
    dni = forms.CharField(label="DNI", max_length=12, min_length=9)
    edad = forms.IntegerField(label="Edad")
    sexo = forms.ChoiceField(label="Sexo", choices=SEXO_CHOICES)
    activo = forms.BooleanField(label="Activo?", required=False)
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), label="Curso")
    turno = forms.ChoiceField(label="Turno", choices=TURNOS)
    fecha_alta = forms.DateField(label="Fecha ingreso", widget=forms.DateInput(
        attrs={'type': 'date'}
    ))