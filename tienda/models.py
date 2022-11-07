from distutils.command.upload import upload
from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, null=False), 
    nombre = models.CharField(max_length=50)
    precioAnterior = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    unidades = models.IntegerField(default=0)
    nuevo = models.BooleanField(default=False, null=False)
    descuento = models.BooleanField(default=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to="productos", null=False)
    popularidad = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre



class Usuario(User):
    segundo_nombre = models.CharField(max_length=40, null=True)
    segundo_apellido = models.CharField(max_length=40, null=True)
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


class Carrito(models.Model):
    idCarrito = models.AutoField(primary_key=True, null=False), 
    idUsuario =  models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    fecha = models.DateField(null=True)
    def __str__(self):
        return str(self.idCarrito)


class DetalleCarrito(models.Model):
    idCarrito =  models.ForeignKey(Carrito, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    subTotal =  models.IntegerField(default=0)
    def __str__(self):
        return str(self.idProducto)


class Favorito(models.Model):
    idFavorito = models.AutoField(primary_key=True, null=False), 
    idUsuario =  models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField(null=True)
    def __str__(self):
        return str(self.idFavorito)

class DetalleFavorito(models.Model):
    idFavorito =  models.ForeignKey(Favorito, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.idFavorito)


class Factura(models.Model):
    idFactura = models.AutoField(primary_key=True, null=False), 
    idUsuario =  models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    fecha = models.DateField(null=True)
    def __str__(self):
        return str(self.idFactura)

class DetalleFactura(models.Model):
    idFactura =  models.ForeignKey(Factura, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    subTotal =  models.IntegerField(default=0)
    def __str__(self):
        return  str(self.idProducto)

    
opciones_consultas =[
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    def _str_(self):
        return self.nombre

class calificar(models.Model):
    rating = models.FloatField(default=0)
    name = models.CharField(max_length=100)
    review = models.TextField(max_length=500, blank=True)
    status = models.BooleanField(default=True)
    """ created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) """
    def _str_(self):
        return self.name

