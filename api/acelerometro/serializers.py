from rest_framework import serializers
from .model.acelerometro import Acelerometro
from .model.leitura import Leitura
from .model.arquivo import Arquivo
from core.serializers import UserSerializer

class ArquivoSimplificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arquivo
        fields = ('dataInicialLeitura', 'frequenciaTempo', 'media', 'desvioPadrao')

class LeituraSimplificadoSerializer(serializers.ModelSerializer):
    #arquivo = ArquivoSerializer()
    class Meta:
        model = Leitura
        fields = ('registro','valor')

class AcelerometroSimplificadoSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Acelerometro
        fields = ('id', 'codigo')


class AcelerometroSerializer(serializers.ModelSerializer):
    arquivos = ArquivoSimplificadoSerializer(source='acelerometro', many=True)
    class Meta:
        model = Acelerometro
        fields = ('__all__')

class LeituraSerializer(serializers.ModelSerializer):
    #arquivo = ArquivoSerializer()
    class Meta:
        model = Leitura
        fields = ('__all__')


class ArquivoSerializer(serializers.ModelSerializer):
    #leituras = LeituraSimplificadoSerializer(source='arquivo', many=True)
    acelerometro = AcelerometroSimplificadoSerializer()
    usuario = UserSerializer()
    class Meta:
        model = Arquivo
        fields = ('__all__')

class ArquivoSerializerCompleto(serializers.ModelSerializer):
    leituras = LeituraSimplificadoSerializer(source='arquivo', many=True)
    # acelerometro = AcelerometroSimplificadoSerializer()
    # usuario = UserSerializer()
    class Meta:
        model = Arquivo
        fields = ('__all__')


