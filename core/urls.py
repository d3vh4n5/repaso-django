from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar_alumnos', views.listar_alumnos, name='listar_alumnos')
]