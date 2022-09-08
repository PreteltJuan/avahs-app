
from django.urls import path
from . import views


urlpatterns = [
    path("home", views.home,  name="home"),
    path("novedades", views.novedades),
    path("descuentos", views.descuentos),
    path("producto/<nombre_p>", views.producto),
    path("resultados", views.resultados),
    path("login", views.login),
    path("registro", views.registro),
    path("carrito", views.carrito, name="carrito"),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="agregar"),
    path('limpiar', views.limpiar_carrito, name="limpiar"),
]

