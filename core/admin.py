from django.contrib import admin
from .models import Alumno, Curso, Docente, Comision, Inscripcion
from .forms import DocenteForm

class CustomAdminSite(admin.AdminSite):
    site_header = "Administracion personalizada"
    site_title= "Administracion para super usuarios"
    index_title = "Admin del mi sitio"
    empty_value_display = "No hay nada"

misitio_admin = CustomAdminSite(name= "miadmin")

class InscripcionInline(admin.TabularInline):
    # model = Comision.alumnos.through
    model = Inscripcion
    extra = 1 # cuantas opciones de carga aparecen por defecto

class AlumnoAdmin(admin.ModelAdmin):

    list_display = ('legajo', 'apellido', 'nombre')
    list_editable = ('apellido', 'nombre')
    list_display_links = ('legajo',)
    search_fields = ['apellido']
    inlines = (InscripcionInline, )

misitio_admin.register(Alumno, AlumnoAdmin) # Sobreescribo el admin
# admin.site.register(Alumno, AlumnoAdmin) # Sobreescribo el admin

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('cuit',)
    form= DocenteForm

# Register your models here.
# admin.site.register(Alumno)
misitio_admin.register(Docente, DocenteAdmin)
# admin.site.register(Docente, DocenteAdmin)
# admin.site.register(Comision)
# admin.site.register(Curso)





@admin.display(description="Nombre del curso en minuscula")
def curso_mayuscula(objeto):
    return f"Curso {objeto.nombre}".upper()

# Otra forma de sobreescribir al admin
# @admin.register(Curso)
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.TextField: {'widget' : widgets.CacTextWidget}
    # }


    # el segundo metodo esta entre comillas porque esta definido dentro del
    # register, el primero esta sin comillas porque esta definidio fuera
    list_display = (curso_mayuscula, 'curso_minuscula',)

    @admin.display(description="Nombre del curso en minuscula")
    def curso_minuscula(self, objeto):
        return f"Curso {objeto.nombre}".lower()

@admin.register(Comision)
class ComisionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio')
    inlines = (InscripcionInline, )
    exclude = ('alumnos', )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "alumnos":
            kwargs["queryset"] = Alumno.objects.filter(legajo__startswith="2").order_by("apellido")
        
        return super().formfield_for_manytomany(db_field, request, **kwargs)

# Registro de ComisionAdmin en misitio_admin
misitio_admin.register(Comision, ComisionAdmin)