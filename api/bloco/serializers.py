from rest_framework import serializers
from .models import Bloco, Acelerometro, Aceleracao

class BlocoSimplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloco
        fields = ('__all__')

class AcelerometroSimplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acelerometro
        fields = ('__all__')

class AceleracaoSimplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aceleracao
        fields = ('__all__')