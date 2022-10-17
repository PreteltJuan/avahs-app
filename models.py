from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precioAnterior = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    unidades = models.IntegerField(default=0)
    nuevo = models.BooleanField(default=False, null=False)
    descuento = models.BooleanField(default=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to="productos", null=False)
    def __str__(self):
        return self.nombre




opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def _str_(self):
        return self.nombre

""" class Review(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    product = models.ForeignKey(Producto, models.CASCADE)
    comment = models.TextField(max_length=250)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)    

 """
class Usuario(User):
    
    #idUsuario = models.AutoField(primary_key=True)
    #primer_nombre = models.CharField(max_length=40, null=True)
    segundo_nombre = models.CharField(max_length=40, null=True)
    #primer_apellido = models.CharField(max_length=40, null=True)
    segundo_apellido = models.CharField(max_length=40, null=True)
    #correo = models.CharField(max_length=100, null=True)
    #clave = models.CharField(max_length=100, null=True)
    direccion = models.CharField(max_length=128)
    barrio = models.CharField(max_length=64)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=16)

    @property
    def primer_nombre(self):
        return self.first_name

    @property
    def primer_apellido(self):
        return self.last_name

    @property
    def correo(self):
        return self.email

    def __str__(self):
        return self.primer_nombre
    
class calificar(models.Model):
    rating = models.FloatField(default=0)
    name = models.CharField(max_length=100)
    review = models.TextField(max_length=500, blank=True)
    status = models.BooleanField(default=True)
    """ created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) """
    def _str_(self):
        return self.subject