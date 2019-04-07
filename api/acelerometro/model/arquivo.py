from django.db import models
from django.contrib.auth.models import User
from .acelerometro import Acelerometro

class Arquivo(models.Model):
    id = models.AutoField(primary_key=True)
    acelerometro = models.ForeignKey(Acelerometro, on_delete=models.CASCADE, related_name='acelerometro')
    dataLancamento = models.DateTimeField(auto_now_add=True)
    dataInicialLeitura = models.DateTimeField()
    frequenciaTempo = models.FloatField()
    qtdeRegistros = models.BigIntegerField()
    media = models.DecimalField(max_digits=10, decimal_places=10, null=True)
    desvioPadrao = models.DecimalField(max_digits=10, decimal_places=10, null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='usuario')

    def __str__(self):
        retorno = []
        retorno.append(self.id)
        retorno.append(" - ")
        retorno.append(self.acelerometro.descricao)
        retorno.append(" / ")
        retorno.append(self.dataLancamento)
        return retorno
