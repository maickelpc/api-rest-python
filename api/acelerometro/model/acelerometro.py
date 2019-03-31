from django.db import models

class Acelerometro(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100, unique=True)
    descricao = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)
    qtdeEixos = models.PositiveSmallIntegerField()
