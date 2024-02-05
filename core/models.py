from django.db import models

# Create your models here.

class Alumno(models.Model):

    nombre = models.CharField(
        null = False,
        blank =False,
        max_length= 64
    )
    apellido = models.CharField(
        null = False,
        blank =False,
        max_length= 64
    )
    edad = models.IntegerField(
        null = False,
        blank= False
    )
    pago_primera_cuota = models.BooleanField()
    turno = models.IntegerField()
    fecha_ingreso = models.DateField()


    def __str__(self):
        return f"{self.nombre} {self.apellido}"