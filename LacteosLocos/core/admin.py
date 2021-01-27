from django.contrib import admin
from .models import Producto, Lacteos
# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display = ['nombre','fecha_elaboracion','fecha_caducidad','tipo']
    search_fields = ['nombre','fecha_caducidad']
    list_filter = ['tipo']
    list_per_page = 10

admin.site.register(Producto, ProductosAdmin)
admin.site.register(Lacteos)