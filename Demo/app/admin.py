from django.contrib import admin
from.models import Marca, Producto, Pintura, Escultura

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=["nombre", "precio", "nuevo", "marca"]
    list_editable=["precio"]
    search_fields=["nombre"]
    list_filter=["marca", "nuevo"]
    list_per_page=2

class PinturaAdmin(admin.ModelAdmin):
    list_display=["nombre", "precio", "nuevo"]
    list_editable=["precio"]

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pintura)
admin.site.register(Escultura)
