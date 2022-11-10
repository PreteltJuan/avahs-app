from django.contrib import admin

from tienda.favorito import Favorito
from .models import DetalleCarrito, DetalleFavorito, Factura, Producto, Usuario, DetalleFactura, Carrito, Favorito
from .models import Contacto
from .models import Review
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio", "idProducto"]
    list_editable = ["precio"]
    search_fields = ["nombre"]

class UsuarioAdmin(admin.ModelAdmin):
 
    list_display = ["first_name", "segundo_nombre"]
    search_fields = ["firts_name", "segundo_nombre"]
    list_per_page = 5
    
class DetalleFacturaAdmin(admin.ModelAdmin):
    list_per_page = 5

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(DetalleFactura, DetalleFacturaAdmin)
admin.site.register(Contacto)
admin.site.register(Carrito)
admin.site.register(DetalleCarrito)
admin.site.register(Review)
admin.site.register(DetalleFavorito)
admin.site.register(Favorito)
