from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=120, verbose_name='Curso: ')
    imagen = models.ImageField(verbose_name="Imagen", default=None, null=True)
    
    def delete(self):
        self.imagen.delete()
        return super().delete()

    class Meta:
        verbose_name_plural ="Los Cursos"   
    def __str__(self):
        return self.nombre
    


class Alumno(models.Model):
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
    dni = models.CharField(
        null = False,
        blank =False,
        max_length= 12,
        default="000000000",
        # unique=True
    )
    edad = models.IntegerField(
        null = False,
        blank= False
    )
    activo = models.BooleanField()
    turno = models.IntegerField(choices=TURNOS)
    fecha_ingreso = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='O')


    def __str__(self):
        return f"{self.nombre} {self.apellido}"