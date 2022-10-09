from distutils.command.upload import upload
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