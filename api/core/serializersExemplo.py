from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import Permission, Role, User

# Serializers define the API representation.

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        # fields = ('__all__')
        fields = ('id', 'permission', 'description', 'active')

class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)
    class Meta:
        model = Role
        fields = ('__all__')


    def createPermissions(self, permissions, role):
        for permission in permissions:
            print(permissions)
            perm,created = Permission.objects.get_or_create(**permission)
            # if permission.id:
            #     perm = Permission.objects.create(**permission)
            # else:
            #     perm = Permission.objects.get(permission.id)
            role.permissions.add(perm)

    def create(self, validated_data):
        permissions = validated_data['permissions']
        print("##############################")
        print(permissions)
        print("##############################")
        del validated_data['permissions']
        role = Role.objects.create(**validated_data)
        self.createPermissions(permissions, role)

        return role


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer();

    class Meta:
        model = User
        fields = ('__all__')

    # def create(self, validated_data):
    #     roles = validated_data['role']
    #     del validated_data['role']
    #     roleUser = Role.objects.get_or_create(**roles)
    #
    #     user = User.objects.create(**validated_data)
    #     user.role = roleUser
    #     user.save()
    #
    #     return user
