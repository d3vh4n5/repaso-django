from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar_alumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('agregar_alumno/', views.agregar_alumno, name="agregar_alumno"),
    path('form_simple/', views.form_simple, name="form_simple"),
]