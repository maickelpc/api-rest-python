from rest_framework import serializers
from .models import Bloco

class BlocoSimplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloco
        fields = ('__all__')

