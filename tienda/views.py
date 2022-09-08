from django.shortcuts import render, redirect
from .carrito import Carrito
from .models import Producto


def home(request):
    productos = Producto.objects.all()
    cant_items = len(productos)
    data = {
        'lista_productos': productos,
        'items': cant_items
    } 
    return render(request, "pages/home.html", data)

def novedades(request):
    productos = Producto.objects.filter(nuevo=True)
    cant_items = len(productos)
    data = {
        'lista_productos': productos,
        'items': cant_items
    } 
    return render(request, "pages/secciones/novedades.html", data)

def descuentos(request):
    productos = Producto.objects.filter(descuento=True)
    cant_items = len(productos)
    data = {
        'lista_productos': productos,
        'items': cant_items
    } 
    return render(request, "pages/secciones/descuentos.html", data)


def tendencias(request):
    return render(request, "pages/secciones/tendencias.html")



def resultados(request):
    return render(request, "pages/resultados.html")

def login(request):
    return render(request, "pages/login.html")

def registro(request):
    return render(request, "pages/registro.html")


def producto(request, nombre_p):
    producto = Producto.objects.get(nombre=nombre_p)
    data = {
        'producto': producto,
    } 
    return  render(request, "pages/producto.html", data)


def carrito(request):
    return  render(request, "pages/carrito.html")

def agregar_producto(request, producto_id):
    carritoCompras = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carritoCompras.agregar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carritoCompras = Carrito(request)
    carritoCompras.limpiar()
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")