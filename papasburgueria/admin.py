from django.contrib import admin
from papasburgueria.models import Hamburguer, Ingrediente, Lucro, Bebida, Comanda, ItensComanda

admin.site.register(Hamburguer)
admin.site.register(Ingrediente)
admin.site.register(Lucro)
admin.site.register(Bebida)

class ItensCompraInline(admin.TabularInline):
    model = ItensComanda

@admin.register(Comanda)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]