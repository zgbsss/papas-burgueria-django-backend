from django.contrib import admin
from papasburgueria.models import Hamburguer, Ingrediente, Lucro, Refrigerante, Compra, ItensCompra

admin.site.register(Hamburguer)
admin.site.register(Ingrediente)
admin.site.register(Lucro)
admin.site.register(Refrigerante)

class ItensCompraInline(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]