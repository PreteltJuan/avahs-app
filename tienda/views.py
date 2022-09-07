from django.shortcuts import render
from django.views.generic import DetailView
from .models import Producto


def home(request):
    return render(request, "pages/home.html")

def novedades(request):
    return render(request, "pages/secciones/novedades.html")

def descuentos(request):
    productos = Producto.objects.all()
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


def carrito(request, nombre_p):
    producto = Producto.objects.get(nombre=nombre_p)
    data = {
        'producto': producto,
    } 
    return  render(request, "pages/carrito.html", data)