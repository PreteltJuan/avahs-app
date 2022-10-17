from pyexpat.errors import messages
import re
from django.shortcuts import render, redirect
from .carrito import Carrito
from .models import Producto, Usuario,Contacto,calificar
from django.contrib.auth import authenticate, login as userlogin, logout as userlogout, get_user_model
from .forms import formularioContacto
from .forms import calificacion

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

def contacto(request):
    data = {
        'form': formularioContacto()
    }
    if request.method == 'POST':
        formulario = formularioContacto(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="mensaje enviado"
        else:
            data["form"]= formulario
            
    return render(request, 'pages/contacto.html',data)

def calificar(request):
    data = {
        'form': calificacion()
    }
    if request.method == 'POST':
        formulario = calificacion(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Reseña enviada"
        else:
            data["form"]= formulario
            
    return render(request, 'pages/calificar.html',data)

    
    

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
    producto = Producto.objects.get(pk=producto_id)
    carritoCompras.agregar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carritoCompras = Carrito(request)
    carritoCompras.limpiar()
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

"""  proximo reseñas de productos
def Review_rate(request):
    if request.method == "GET":
        prod_id = request.GET.get('prod_id')
        product = product.objects.get(id=prod_id)
        comment = request.GET.get('comment')
        rate = request.GET.get('rate')
        user = request.user
        Review(user=user,product=product,comment=comment,rate=rate).save()
        return redirect('prodcut_detail', id=prod_id) 
             if request.method == 'POST':
        try:
            reviews = calificar.objects.get(user__id=request.user.id)
            form = calificacion(request.POST, instance=reviews)
            messages.success(request, 'Gracias! su reseña a sido actualizada')
            return redirect()
        except calificar.DoesNotExist:
            form = calificacion(request.POST)
            if form.is_valid():
                data= calificacion()
                data.subject =form.cleaned_data['subject']
                data.rating =form.cleaned_data['rating'] 
                data.review =form.cleaned_data['review']
                data.save()
                messages.success(request, 'Gracias! su reseña a sido publicada')
                return render(request, "pages/secciones/calificar.html") """
                
                

