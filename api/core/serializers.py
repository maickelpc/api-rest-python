from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

from .models import Permission, Role, User

# Serializers define the API representation.

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('__all__')
        #fields = ('url', 'username', 'email', 'is_staff')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
