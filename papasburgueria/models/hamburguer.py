from django.db import models
from .ingrediente import Ingrediente

class Hamburguer(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank= True)
    ingredientes = models.ForeignKey(Ingrediente, on_delete=models.PROTECT, related_name="hamburguer", null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.preco}"