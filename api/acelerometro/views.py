import datetime
import random
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.db import transaction
from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.core.files import temp as tempfile 
from django.core.files.uploadedfile import UploadedFile

from .model.acelerometro import Acelerometro
from .model.leitura import Leitura
from .model.arquivo import Arquivo
from django.contrib.auth.models import User
from .serializers import AcelerometroSerializer, ArquivoSerializerCompleto, ArquivoSerializer, LeituraSerializer


from rest_framework.parsers import MultiPartParser, FormParser



# Create your views here.

class AcelerometroViewSet(viewsets.ModelViewSet):
    queryset = Acelerometro.objects.all()
    serializer_class = AcelerometroSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','codigo')


class LeituraViewSet(viewsets.ModelViewSet):
    queryset = Leitura.objects.all()
    serializer_class = LeituraSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','arquivo__id')
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000
    



class ArquivoViewSet(viewsets.ModelViewSet):
    queryset = Arquivo.objects.all()
    serializer_class = ArquivoSerializer
    parser_classes = (MultiPartParser, FormParser,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','usuario__id')

    @action(methods=['get'], detail=True)
    def leituras(self, request, pk):    
        arquivo = Arquivo.objects.filter(pk=pk).get()
        serializer = ArquivoSerializerCompleto(arquivo)
        
        return Response(serializer.data)
        


    @action(methods=['post'], detail=False)
    def upload(self, request):
        
        id = 0
        try:
            
            with transaction.atomic():
                acelerometroId = request.POST.get('acelerometro')
                acelerometro = Acelerometro.objects.filter(pk=acelerometroId).get()
                
                fileUpload = UploadedFile(request.FILES['file'])

                arquivo = Arquivo()
                arquivo.acelerometro = acelerometro

                arquivo.dataInicialLeitura = datetime.datetime.now()
                arquivo.frequenciaTempo = random.random()
                arquivo.qtdeRegistros = 0
                arquivo.media = random.random()
                arquivo.desvioPadrao = random.random()
                arquivo.usuario = request.user
                arquivo.save()

                indiceLeitura = 0
                soma = 0
                l = 0
                for linha in fileUpload:
                    if(l > 12):
                        aux = str(linha)
                        aux = aux.rstrip().lstrip()
                        aux = aux.replace("b' ", "")
                        aux = aux.replace("\\r\\n'","")
                        x = aux.split(" ")
                        # print(x)
                        for n in x:
                            valor = n
                            print(n)
                            leitura = Leitura()
                            leitura.dataLeitura = datetime.datetime.now()
                            leitura.eixo = 1
                            leitura.arquivo = arquivo
                            leitura.registro = indiceLeitura
                            # leitura.valor = valor  # Aqui substitui pelo valor em notacaocientifica convertido
                            leitura.valor = random.random()                           
                            leitura.save()
                            indiceLeitura +=1
                    l += 1
                arquivo.qtdeRegistros = indiceLeitura+1
                # arquivo.media = 0
                # arquivo.desvioPadrao = 0
                arquivo.save()
                id = arquivo.id
            return Response({id})
        except ValueError:
            return Response({ValueError}, 400)
    
