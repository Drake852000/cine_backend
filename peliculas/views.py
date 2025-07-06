from rest_framework import viewsets
from .models import (
    Pelicula,
    Sala,
    Funcion,
    Cine,
    Producto,
    Promocion,
    Reserva
)
from .serializers import (
    PeliculaSerializer,
    SalaSerializer,
    FuncionSerializer,
    CineSerializer,
    ProductoSerializer,
    PromocionSerializer,
    ReservaSerializer
)

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class FuncionViewSet(viewsets.ModelViewSet):
    queryset = Funcion.objects.all()
    serializer_class = FuncionSerializer

class CineViewSet(viewsets.ModelViewSet):
    queryset = Cine.objects.all()
    serializer_class = CineSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PromocionViewSet(viewsets.ModelViewSet):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
