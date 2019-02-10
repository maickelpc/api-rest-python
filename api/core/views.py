from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PermissionSerializer, RoleSerializer, UserSerializer
from .models import Permission, Role, User

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.select_related('role').order_by('email').all()
    serializer_class = UserSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.prefetch_related('permissions').all()
    serializer_class = RoleSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
