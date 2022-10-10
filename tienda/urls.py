
from django.urls import path
from . import views


urlpatterns = [
    path("home", views.home,  name="home"),
    path("novedades", views.novedades, name="novedades"),
    path("descuentos", views.descuentos, name="descuentos"),
    path("producto/<nombre_p>", views.producto),
    path("resultados", views.resultados, name="resultados"),
    path("login", views.login),
    path("registro", views.registro),
    path("carrito", views.carrito, name="carrito"),
    path('agregarCarrito/<int:producto_id>/', views.agregar_producto_carrito, name="agregarAlCarrito"),
    path('agregarFavoritos/<int:producto_id>/', views.agregar_producto_favoritos, name="agregarAFavoritos"),
    path('eliminarCarrito/<int:producto_id>/', views.eliminar_producto_carrito, name="eliminarCarrito"),
    path('eliminarFavorito/<int:producto_id>/', views.eliminar_producto_favoritos, name="eliminarFavorito"),
    path('limpiar', views.limpiar_carrito, name="limpiar"),
]

