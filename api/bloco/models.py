from django.db import models

class Bloco(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100, unique=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo;


class Acelerometro(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=100, unique=True)
    descricao = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo;

class Aceleracao(models.Model):
    id = models.AutoField(primary_key=True)
    dataInicio = models.DateTimeField()
    acrescimoSegundos = models.FloatField()
    dataReal = models.DateTimeField()
    orientacao = models.CharField(max_length=1)
    aceleracao = models.FloatField()
    leitura = models.BigIntegerField()
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE, related_name='aceleracao_bloco')
    acelerometro = models.ForeignKey(Acelerometro, on_delete=models.CASCADE, related_name='aceleracao_acelerometro')
