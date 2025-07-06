from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Cine(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.IntegerField()  # en minutos
    genero = models.CharField(max_length=50)
    clasificacion = models.CharField(max_length=10, default='PG-13')
    sinopsis = models.TextField(default='Sin descripción disponible')
    imagen = models.ImageField(upload_to='peliculas/', blank=True, null=True)
    fecha_estreno = models.DateField(default=timezone.now)
    es_preventa = models.BooleanField(default=False)
    es_proximamente = models.BooleanField(default=False)


class Sala(models.Model):
    numero = models.IntegerField()
    capacidad = models.IntegerField()
    cine = models.ForeignKey(Cine, on_delete=models.CASCADE, related_name="salas")


class Funcion(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()


class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=6, decimal_places=2)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='confirmado')  # cancelado, etc.

class Promocion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='promociones/', blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activa = models.BooleanField(default=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    tipo = models.CharField(max_length=50)  # Ej: combo, bebida, snack
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

