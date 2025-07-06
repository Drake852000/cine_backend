from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PeliculaViewSet,
    SalaViewSet,
    FuncionViewSet,
    CineViewSet,
    ProductoViewSet,
    PromocionViewSet,
    ReservaViewSet
)

router = DefaultRouter()
router.register('peliculas', PeliculaViewSet)
router.register('salas', SalaViewSet)
router.register('funciones', FuncionViewSet)
router.register('cines', CineViewSet)
router.register('productos', ProductoViewSet)
router.register('promociones', PromocionViewSet)
router.register('reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
