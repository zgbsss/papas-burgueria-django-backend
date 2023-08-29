from django.db import models
from usuario.models import Usuario
from papasburgueria.models import Ingrediente, Hamburguer, Bebida

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        COMANDA = (1, "Comanda",)
        REALIZADO = (2, "Realizado",)
        PAGO = (3, "Pago",)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.COMANDA)

class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT, related_name="+")
    hamburguer = models.ForeignKey(Hamburguer, on_delete=models.PROTECT, related_name="+")
    bebida = models.ForeignKey(Bebida, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)