
from .models import *
from .serializers import ArquivoFddSimplificadoSerializer
import json, codecs
from pprint import pprint
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.files.uploadedfile import UploadedFile

from pylab import *


class ArquivoFddViewSet(viewsets.ModelViewSet):
    queryset = ArquivoFdd.objects.all()
    serializer_class = ArquivoFddSimplificadoSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('id','codigo')

    codigo = models.CharField(max_length=30)
    arquivo = models.FileField()
    data = models.DateTimeField()


    def create(self, request, *args, **kwargs):
        # Codigo

        print(request.POST.get('canais'))
        print(datetime.datetime.strptime(request.POST.get('data'), '%d/%m/%Y %H:%M:%S'))
        print(int(request.POST.get('canais')))


        arquivo = ArquivoFdd();
        arquivo.arquivo = UploadedFile(request.FILES['arquivo']);
        arquivo.codigo = request.POST.get('codigo')
        arquivo.canais = int(request.POST.get('canais'))
        arquivo.descricao = request.POST.get('descricao')
        arquivo.frequencia = request.POST.get('frequencia')
        arquivo.dataInicio = datetime.datetime.strptime(request.POST.get('data'), '%d/%m/%Y %H:%M:%S')
        arquivo.data = datetime.datetime.now()

        arquivo.save()

        return Response({arquivo.id}, 200)
        # #deixe o Django fazer a magica dele
        # return super(ArquivoFddViewSet, self).create(request, *args, **kwargs)


    @action(methods=['post'], detail=False)
    def grafico(self, request):
        json_dict = json.loads(request.body)
        graus = int(json_dict['analisar'])
        fourierSize = int(json_dict['fourier'])
        arq = int(json_dict['id'])
        arq = ArquivoFdd.objects.get(pk=arq)
        dominio = arq.canais
        arquivo = genfromtxt(arq.arquivo, delimiter=",")
        print(arq.arquivo)
        print("CARAIO")
        print(arquivo)
        fdd = FDD.objects.get(pk=1)
        frequency, eigen_values = fdd.system_frequency(dominio, fourierSize, arquivo, graus)

        print(frequency)
        print(eigen_values)

        # return Response({frequency.__str__(),eigen_values.__str__()}, 200)
        return Response({arquivo.__str__()}, 200)


