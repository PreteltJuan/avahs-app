
from django.shortcuts import render, redirect
from datetime import date
from .favorito import Favorito
from .carrito import Carrito
from .models import DetalleFactura, Producto, Usuario, Factura
from django.contrib.auth import authenticate, login as userlogin, logout as userlogout, get_user_model


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
    text = request.GET.get('search', '')
    producto = Producto.objects.filter(nombre__icontains=text)
    items = len(producto)
    data = {
        'productos': producto,
        'items': items,
    } 
    return  render(request, "pages/resultados.html", data)

def login(request):

    if request.user.is_authenticated:
        return redirect("home")

    error = False
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    if username and password:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            userlogin(request, user)
            return redirect("home")
        else:
            error = True

    return render(request, "pages/registro_login/login.html", {
        "error": error
    })

def logout(request):
    userlogout(request)
    return redirect("login")

def registro(request):
    error=False
    nombre_campos = [
        "primer_nombre",
        "segundo_nombre",
        "primer_apellido",
        "segundo_apellido",
        "nombre_usuario",
        "correo",
        "clave",
        "barrio",
        "direccion",
        "fecha",
        "sexo",
    ]

    campos = {
        nombre: request.POST.get(nombre, "")
        for nombre in nombre_campos
    }

    crear_usuario = campos.get("nombre_usuario")
    if crear_usuario:
        campos.update({
            "first_name":campos.get("primer_nombre"),
            "last_name":campos.get("primer_apellido"),
            "username":campos.get("nombre_usuario"),
            "email":campos.get("correo"),
            "password":campos.get("clave"),
            "fecha_nacimiento":campos.get("fecha")
        })

        borrar_campos = ("primer_nombre","primer_apellido","nombre_usuario","correo","clave","fecha")

        for campo in borrar_campos:
            campos.pop(campo, None)

        user = Usuario.objects.create_user(**campos)

        if user is not None:
            userlogin(request, user)
            return redirect("home")
        else:
            error = True

    return render(request, "pages/registro_login/registro.html", {"error":error})

def producto(request, nombre_p ):
    producto = Producto.objects.get(nombre=nombre_p)
    data = {
        'producto': producto,
    } 
    return  render(request, "pages/producto.html", data)

def carrito(request):
    return  render(request, "pages/carrito.html")

def compra(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    usuario = Usuario.objects.get(username=request.user)
    
    data = {
        'usuario': usuario,
    } 
    return render(request, "pages/compra.html", data )


def agregar_producto_carrito(request, producto_id):
    carritoCompras = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carritoCompras.agregar(producto)
    return redirect("carrito")

def agregar_producto_favoritos(request, producto_id):
    favoritos = Favorito(request)
    producto = Producto.objects.get(id=producto_id)
    favoritos.agregar(producto)
    producto.popularidad += 1
    producto.save()
    return redirect(request.META.get('HTTP_REFERER'))

def limpiar_carrito(request):
    carritoCompras = Carrito(request)
    carritoCompras.limpiar()
    return redirect("carrito")

def eliminar_producto_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def eliminar_producto_favoritos(request, producto_id):
    favoritos = Favorito(request)
    producto = Producto.objects.get(id=producto_id)
    favoritos.eliminar(producto)
    return redirect(request.META.get('HTTP_REFERER'))

def actualizar_carrito(request):
    carro = Carrito(request)

    for key in carro.carrito.keys():
        newCant =  request.GET.get(key, '')
        carro.actualizarCantidad(key, int(newCant))

    carro.actualizarSubTotal()
    return redirect("carrito")
    
def realizar_compra(request):
    usuario = Usuario.objects.get(username=request.user)
    carritoCompras = Carrito(request)
    factura = Factura(
        idUsuario = usuario,
        total = carritoCompras.subTotal,
        fecha = date.today())
    factura.save()
    for key,value in carritoCompras.carrito.items():
        producto = Producto.objects.get(id = key)
        detallerFactura =  DetalleFactura(
            idFactura = factura,
            idProducto = producto,
            precio = producto.precio,
            cantidad = value["cantidad"],
            subTotal = value["acumulado"],
        )
        detallerFactura.save()
    
    carritoCompras.limpiar()
    
    return redirect("home")