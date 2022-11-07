from django.contrib import admin
from .models import Factura, Producto, Usuario, DetalleFactura
from .models import Contacto
from .models import Review
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio", "idProducto"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_per_page = 5

class UsuarioAdmin(admin.ModelAdmin):
 
    list_display = ["first_name", "segundo_nombre"]
    search_fields = ["firts_name", "segundo_nombre"]
    list_per_page = 5
    
class FacturaAdmin(admin.ModelAdmin):
    list_display = [ "total", "fecha"]
    search_fields = [ "total", "fecha"]
    list_per_page = 5

class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = [ "precio", "cantidad", "subTotal"]
    search_fields = [ "total", "fecha"]
    list_per_page = 5

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(DetalleFactura, DetalleFacturaAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(Contacto)
admin.site.register(Review)
