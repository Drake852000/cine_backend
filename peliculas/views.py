from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Pelicula, Sala, Funcion
from .serializers import PeliculaSerializer, SalaSerializer, FuncionSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class FuncionViewSet(viewsets.ModelViewSet):
    queryset = Funcion.objects.all()
    serializer_class = FuncionSerializer
