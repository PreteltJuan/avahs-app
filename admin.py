from django.contrib import admin
from .models import Producto
from .models import Usuario
from .models import Contacto
from .models import calificar
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
    
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["first_name", "segundo_nombre"]
    
    

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Contacto)
admin.site.register(calificar)