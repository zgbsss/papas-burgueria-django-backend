from django.db import models

class Bebida(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank= True)

    def __str__(self):
        return f"{self.nome}, {self.descricao}, {self.preco}"