from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

from .models import User

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        #fields = ('url', 'username', 'email', 'is_staff')
