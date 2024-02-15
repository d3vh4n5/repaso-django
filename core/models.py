from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=120, verbose_name='Curso: ')
    imagen = models.ImageField(verbose_name="Imagen", default=None, null=True)
    baja= models.BooleanField(default=False)

    def delete(self):
        self.imagen.delete()
        return super().delete()

    class Meta:
        verbose_name_plural ="Los Cursos"   

    def __str__(self):
        return self.nombre
    
    def soft_delete(self):
        self.baja = True
        self.save()

    def restore(self):
        self.baja = False
        self.save()
    
class Persona(models.Model):
    

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
    # edad = models.IntegerField(
    #     null = False,
    #     blank= False
    # )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='O')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    # Agregar esto hace que la clase Persona no se registre en la base de
    # datos como una tabla independiente,  sino que actua como una clase 
    # base abstracta para otros modelos. Lo cual también previene que se
    # genere el campo "persona_ptr" en las entidedes que hereden de esta
    class Meta:
        abstract = True



class Alumno(Persona):
    class Meta:
        verbose_name_plural = _("Alumnos")

    

    legajo = models.CharField(null = True, max_length=20, default="-----")
    activo = models.BooleanField()
    
    fecha_ingreso = models.DateField()
    #curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)

    # Permitir que persona_ptr sea nulo
    # Este campo se generó cuando quite información de alumno para ponerla 
    # en la clase abstracta Persona
    # persona_ptr = models.OneToOneField(
    #     Persona,
    #     on_delete=models.CASCADE,
    #     parent_link=True,
    #     primary_key=True,
    #     related_name='+',
    #     null=True
    # )

class Docente(Persona):
    class Meta:
        verbose_name_plural = _("Docentes")
    
    cuit = models.CharField(max_length=100, verbose_name='Cuit')

class Comision(models.Model):
    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche"),
    )

    class Meta:
        verbose_name_plural = _("Comisiones")

    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(null=True, verbose_name ="Descripcion")
    fecha_inicio = models.DateTimeField(verbose_name='Fecha de inicio')
    turno = models.IntegerField(choices=TURNOS, default=3)
    portada = models.ImageField(upload_to='imagenes/comisiones/', null=True, verbose_name='Portada')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True)
    alumnos = models.ManyToManyField(Alumno) 
    # Esto genera una tabla aparte para las relaciones, pero se pone en esta clase
    # porque será desde la cual se elijan los las entidades relacionadas a esta

    def __str__(self):
        return self.nombre
