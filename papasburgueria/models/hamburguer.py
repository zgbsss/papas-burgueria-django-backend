from django.db import models

class Hamburguer(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank= True)

    def __str__(self):
        return f"{self.nome} - {self.preco}"