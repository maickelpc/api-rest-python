
from .models import *
from .serializers import ArquivoSimplificadoSerializer
import json, codecs
from pprint import pprint
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.files.uploadedfile import UploadedFile

from pylab import *


class ArquivoViewSet(viewsets.ModelViewSet):
    queryset = Arquivo.objects.all()
    serializer_class = ArquivoSimplificadoSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('id','codigo')

    codigo = models.CharField(max_length=30)
    arquivo = models.FileField()
    data = models.DateTimeField()

    def create(self, request, *args, **kwargs):

        self.codigo = request.POST.get('codigo')
        self.data = request.POST.get('data')
        self.arquivo = UploadedFile(request.FILES['arquivo'])


        #deixe o Django fazer a magica dele
        return super(Arquivo, self).create(request, *args, **kwargs)

    @action(methods=['post'], detail=False)
    def grafico(self, request):
        json_dict = json.loads(request.body)
        print(json_dict)
        graus = int(json_dict['graus'])
        fourierSize = int(json_dict['fourier'])
        dominio = int(json_dict['dominio'])
        arq = int(json_dict['id'])

        arq = Arquivo.objects.get(pk=arq)
        arquivo = genfromtxt(arq.arquivo, delimiter=",")
        fdd = FDD.objects.get(pk=1)
        frequency, eigen_values = fdd.system_frequency(dominio, fourierSize, arquivo, graus)

        return Response({frequency.__str__(),eigen_values.__str__()}, 200)



