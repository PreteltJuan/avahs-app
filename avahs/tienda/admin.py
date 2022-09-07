from django.contrib import admin
from .models import Producto
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio" ]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_per_page = 5
    

admin.site.register(Producto,ProductoAdmin)