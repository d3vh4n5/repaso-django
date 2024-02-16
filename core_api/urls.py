from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core_api import views

router = DefaultRouter()
# router.register(r'alumnos', views.AlumnoViewSet, basename='alumno')
router.register(r'/alumnos', views.AlumnoViewSet, basename='alumnos')

urlpatterns = [
    # Rutas API
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/'),
]