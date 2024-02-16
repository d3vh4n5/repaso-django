from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.my_login, name='my_login'),
    path('register/', views.user_register, name='user_register'),
    path('logout/', views.my_logout, name='my_logout'),

    # a mie ste logout no me funciono
    # path('logout/',
    #     auth_views.LogoutView.as_view(template_name='index.html'),
    #     name='my_logout'),

    path('listar_alumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('agregar_alumno/', views.agregar_alumno, name="agregar_alumno"),
    path('form_simple/', views.form_simple, name="form_simple"),
]