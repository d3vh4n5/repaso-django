from django import forms

class AgregarAlumno(forms.Form):

    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche"),
    )

    nombre = forms.CharField(label="Nombre", max_length=20, min_length=3)
    apellido = forms.CharField(label="Apellido", max_length=20, min_length=2)
    edad = forms.IntegerField(label="Edad")
    pago = forms.BooleanField(label="Pagó primera cuota", required=False)
    turno = forms.ChoiceField(label="Turno", choices=TURNOS)
    fecha_alta = forms.DateField(label="Fecha ingreso", widget=forms.DateInput(
        attrs={'type': 'date'}
    ))