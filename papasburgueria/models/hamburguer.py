from django.db import models
from papasburgueria.models import Ingrediente

class Hamburguer(models.Model):
    nome = models.CharField(max_length=255)
    ingrediente = models.ForeignKey (Ingrediente, on_delete=models.PROTECT, related_name="ingredientes")
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank= True)

    def __str__(self):
        return f"{self.nome} - {self.preco}"