from django.db import models
from .ingrediente import Ingrediente
from uploader.models import Image

class Hamburguer(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank= True)
    ingredientes = models.ManyToManyField(Ingrediente, related_name="hamburguer")
    avaliacao = models.DecimalField(max_digits=5, decimal_places= 0, default=0, null= True, blank= True)
    image = models.ForeignKey(Image, related_name="+", on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.nome} - {self.preco}"    