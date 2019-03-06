from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PermissionSerializer, RoleSerializer, UserSerializer
from .models import Permission, Role, User
from rest_framework.decorators import action


# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.select_related('role').order_by('email').all()
    serializer_class = UserSerializer

    def get_queryset(self):
        # Filtragem manual, boa para casos especiais
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        email = self.request.query_params.get('email', None)

        queryset = User.objects
        if id:
            queryset = queryset.filter(pk=id)
            return queryset

        if nome: # Usando icontains pega o campo por case insensitive
            queryset = queryset.filter(firstName__icontains=nome)

        if email:
            queryset = queryset.filter(email__icontains=email)

        return queryset


    def list(self, request, *args, **kwargs):
        #Codigo com suas regras


        #deixe o Django fazer a magica dele
        return super(UserViewSet, self).list(request, *args, **kwargs)


    # def create(self, request, *args, **kwargs):
    #     # Codigo com regrasabs
    #
    #     #deixe o Django fazer a magica dele
    #     return super(UserViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Codigo com regrasabs

        #deixe o Django fazer a magica dele
        return super(UserViewSet, self).destroy(request, *args, **kwargs)


    def retrive(self, request, *args, **kwargs):
        #Codigo com regras

        #deixe o Django fazer a magica dele
        return super(UserViewSet, self).retrive(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        #codigo com regras


        #deixe o Django fazer a magica dele
        return super(UserViewSet, self).update(request, *args, **kwargs)


    def partial_update(self, request, *args, **kwargs):
        #codigo com regras


        #deixe o Django fazer a magica dele
        return super(UserViewSet, self).partial_update(request, *args, **kwargs)


    @action(methods=['get'], detail=True)
    def resetPassword(self, request, pk=None):

        user = User.objects.get(id=pk)
        user.password = '1234567890'
        user.save();
        return Response({'Senha Alterada do usuário ID: ' + user.firstName})
        #return Response({'Senha Alterada do usuário ID: ' + pk})





class RoleViewSet(viewsets.ModelViewSet):
#    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('description', 'role', )
    #filter_fields = ('active') #Filter_backend

    def get_queryset(self):
        return Role.objects.all()

    def create(self, request, *args, **kwargs):
        # Codigo com regrasabs

        #deixe o Django fazer a magica dele
        return super(UserViewSet, self).create(request, *args, **kwargs)





class PermissionViewSet(viewsets.ModelViewSet):
#    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    filter_backends = (DjangoFilterBackend,)
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    filter_fields = ('active','description','permission') #Filter_backend
    #lookup_field = 'permission';

    def get_queryset(self):
        return Permission.objects.all()
