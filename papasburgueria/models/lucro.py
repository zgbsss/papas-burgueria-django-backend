from django.db import models

class Lucro(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank= True)
    semana = models.CharField(max_length=255)
    mes = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.mes}, {self.semana}, {self.valor}"