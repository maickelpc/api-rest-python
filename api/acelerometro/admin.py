from django.contrib import admin
from .model.acelerometro import Acelerometro
from .model.leitura import Leitura
from .model.arquivo import Arquivo
# Register your models here.


admin.site.register(Leitura)
admin.site.register(Acelerometro)
admin.site.register(Arquivo)
# Register your models here.
