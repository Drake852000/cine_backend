from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PeliculaViewSet, SalaViewSet, FuncionViewSet

router = DefaultRouter()
router.register('peliculas', PeliculaViewSet)
router.register('salas', SalaViewSet)
router.register('funciones', FuncionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
