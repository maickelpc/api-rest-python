from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from .models import  Profile
from django.contrib.auth.models import User

# Serializers define the API representation.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('__all__')
