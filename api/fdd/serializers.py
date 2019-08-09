from rest_framework import serializers
from .models import Arquivo

class ArquivoSimplificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arquivo
        fields = ('__all__')
