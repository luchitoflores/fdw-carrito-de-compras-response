from principal.models import Familia, Fabricante, Recambio, CarritoDeCompra
from django.contrib import admin


class FamiliaAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


class RecambioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fabricante', 'precio']
    list_filter = ['fabricante']
    readonly_fields = ['slug']


class CarritoDeCompraAdmin(admin.ModelAdmin):
    list_display = ['user', 'recambio', 'unidades', 'precio']


admin.site.register(Fabricante)
admin.site.register(Familia, FamiliaAdmin)
admin.site.register(Recambio, RecambioAdmin)
admin.site.register(CarritoDeCompra, CarritoDeCompraAdmin)
