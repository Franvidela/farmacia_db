from django.contrib import admin
from django.contrib.admin import register

from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.
# @admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_display_links = ['nombre']
    # list_filter = ('nombre')

# @admin.register(DirectorGeneral)
class DirectorioGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    list_display_links = ['nombre']
    list_filter = ('nombre', 'laboratorio')

# @register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'fecha_fabricacion', 'precio_costo', 'precio_venta')
    list_display_links = ['nombre']
    list_filter = ('nombre', 'laboratorio')   

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorioGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
