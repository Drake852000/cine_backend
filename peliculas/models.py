from django.db import models

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.IntegerField()  # en minutos
    genero = models.CharField(max_length=50)

class Sala(models.Model):
    numero = models.IntegerField()
    capacidad = models.IntegerField()

class Funcion(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()