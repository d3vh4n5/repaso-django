from django.contrib import admin
from .models import Alumno, Curso, Docente, Comision

class AlumnoAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Alumno, AlumnoAdmin) # Sobreescribo ela dmin

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(Comision)
admin.site.register(Curso)


# Otra forma de sobreescribir al admin
# @admin.register(Curso)
# class PEPE(admin.ModelAdmin):
#     pass