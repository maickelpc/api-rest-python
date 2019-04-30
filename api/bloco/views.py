from django.shortcuts import render
import datetime
import random
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.db import transaction
from django.db.models import StdDev, Avg
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.core.files import temp as tempfile
from django.core.files.uploadedfile import UploadedFile


from .serializers import BlocoSimplesSerializer
from .models import Bloco

class BlocoViewSet(viewsets.ModelViewSet):
    queryset = Bloco.objects.all()
    serializer_class = BlocoSimplesSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('codigo','localizacao', 'descricao')