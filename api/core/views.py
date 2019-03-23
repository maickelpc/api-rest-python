from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProfileSerializer, UserSerializer
from .models import Profile
from django.contrib.auth.models import User

from rest_framework.decorators import action


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['user'] = user.username
        token['firstName'] = user.first_name
        token['lastName'] = user.last_name
        token['email'] = user.email
        # profile = Profile.objects.get(id=user.id)
        # print(profile.image);
        # token['image'] = profile.image
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('email').all()
    serializer_class = UserSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('username', 'name', 'last_name', 'email' )


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.select_related('user').all()
    serializer_class = ProfileSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email' )
