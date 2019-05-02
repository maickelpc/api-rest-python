from django.shortcuts import render
import datetime
from datetime import timedelta
# from dateutil.parser import parse
import random
from django.shortcuts import render
from django.db import transaction
from django.db.models import StdDev, Avg
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from django.core.files import temp as tempfile
from django.core.files.uploadedfile import UploadedFile


from .serializers import BlocoSimplesSerializer, AcelerometroSimplesSerializer, AceleracaoSimplesSerializer
from .models import Bloco, Acelerometro, Aceleracao

class BlocoAcelerometroViewSet(viewsets.ModelViewSet):
    queryset = Acelerometro.objects.all()
    serializer_class = AcelerometroSimplesSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('codigo', 'descricao')

class BlocoAceleracaoViewSet(viewsets.ModelViewSet):
    queryset = Aceleracao.objects.all()
    serializer_class = AceleracaoSimplesSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('id')

class BlocoViewSet(viewsets.ModelViewSet):
    queryset = Bloco.objects.all()
    serializer_class = BlocoSimplesSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('codigo','descricao')

    @action(methods=['post'], detail=False)
    def upload(self, request):
        inicio = datetime.datetime.now()
        id = 0
        try:
            with transaction.atomic():
                blocoId = request.POST.get('blocoId')
                acelerometroId = request.POST.get('acelerometroId')
                fileUpload = UploadedFile(request.FILES['arquivo'])
                dataHora =  datetime.datetime.strptime(request.POST.get('dataHoraInicio'),  '%Y-%m-%d %H:%M:%S')
                
                bloco = Bloco.objects.filter(pk=blocoId).get()
                acelerometro = Acelerometro.objects.filter(pk=acelerometroId).get()
                                
                a = 1 #Aceleracao lida

                for linha in fileUpload:
                    aux = str(linha)
                    aux = aux.rstrip().lstrip()
                    
                    aux = aux.replace("b'", "")
                    aux = aux.replace("\\r\\n'","")
                    
                    leituras = aux.split("\\t")
                    
                    leituras.pop()          # Remove o ultimo item da tabulação que vem vazio no arquivo
                    tempoStr = leituras.pop(0) # Remove o primeiro item do array para incrementar o tempo inicial
                    tempo = float(tempoStr)
                    
                    indice = 1;
                    for leitura in leituras:
                        
                        aceleracao = Aceleracao();
                        aceleracao.bloco = bloco
                        aceleracao.acelerometro= acelerometro
                        aceleracao.dataInicio = dataHora
                        aceleracao.leitura = a
                        aceleracao.acrescimoSegundos = tempo
                        aceleracao.dataReal = dataHora + timedelta(seconds=tempo)

                        if indice == 1:
                            aceleracao.orientacao = 'V'
                        elif indice == 2:
                            aceleracao.orientacao = 'L'
                        else:
                            aceleracao.orientacao = 'T'
                            
                        aceleracao.aceleracao = float(leitura)
                        aceleracao.save()
                        
                        if(indice == 3):
                            a += 1
                            indice = 1
                        else:
                            indice += 1
   
                # arquivo.qtdeRegistros = indiceLeitura+1
                # media = Leitura.objects.filter(arquivo=arquivo).aggregate(valor=Avg('valor'))
                # desvioPadrao = Leitura.objects.filter(arquivo=arquivo).aggregate(valor=StdDev('valor'))
                # arquivo.media = media['valor']
                # arquivo.desvioPadrao = desvioPadrao['valor']

                # arquivo.save()
                # id = arquivo.id
            fim = datetime.datetime.now()
            print(inicio);
            print(fim);
            print (fim - inicio)
            return Response({tempo: fim - inicio})
        except ValueError:
            return Response({ValueError}, 400)