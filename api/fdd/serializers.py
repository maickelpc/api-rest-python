from rest_framework import serializers
from .models import ArquivoFdd

class ArquivoFddSimplificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArquivoFdd
        fields = ('__all__')
