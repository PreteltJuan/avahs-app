
from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home,  name="home"),
    path("novedades/", views.novedades, name="novedades"),
    path("descuentos/", views.descuentos, name="descuentos"),
    path("contacto/", views.contacto,  name="contacto"),
    path("calificar/", views.calificar,  name="calificar"),
    path("producto/<nombre_p>/", views.producto),
    path("resultados/", views.resultados, name="resultados"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("registro/", views.registro, name="registro"),
    path("carrito/", views.carrito, name="carrito"),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="agregar"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar"),
    path('limpiar/', views.limpiar_carrito, name="limpiar"),
]

