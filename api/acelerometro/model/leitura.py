from django.db import models
from .acelerometro import Acelerometro
from .arquivo import Arquivo

class Leitura(models.Model):
    id = models.AutoField(primary_key=True)
    dataLeitura = models.DateTimeField()
    eixo = models.PositiveSmallIntegerField()
    arquivo = models.ForeignKey(Arquivo, on_delete=models.CASCADE, related_name='arquivo')
    registro = models.BigIntegerField() 
    valor = models.DecimalField(max_digits=10, decimal_places=10, null=True)
