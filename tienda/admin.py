from django.contrib import admin
from .models import Producto, Usuario, Factura, ProductoComprado
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio", "idProducto"]
    list_editable = ["precio"]
    search_fields = ["nombre"]

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["first_name", "segundo_nombre", "barrio"]
    search_fields = ["firts_name", "segundo_nombre"]

class FacturaAdmin(admin.ModelAdmin):
    list_display = ["idFactura", "idUsuario", "precio"]

class ProductoCompradoAdmin(admin.ModelAdmin):
    list_display = ["idProductoComprado", "idFactura", "idProducto", "cantidad"]

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(ProductoComprado, ProductoCompradoAdmin)

