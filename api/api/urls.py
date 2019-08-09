from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
#from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from core.views import ProfileViewSet, UserViewSet, MyTokenObtainPairView
from acelerometro.views import LeituraViewSet, ArquivoViewSet, AcelerometroViewSet
from bloco.views import BlocoViewSet, BlocoAceleracaoViewSet, BlocoAcelerometroViewSet
from fdd.views import ArquivoViewSet


router = routers.DefaultRouter();
router.register('profile',ProfileViewSet, 'Profile')
router.register('user',UserViewSet,'User')
router.register('fdd/arquivo',ArquivoViewSet,'Arquivo')
# router.register('dados/arquivo',ArquivoViewSet, 'Arquivo')
router.register('dados/leitura',LeituraViewSet,'Leitura')
#router.register('acelerometro',AcelerometroViewSet, 'Acelerometro')
router.register('bloco',BlocoViewSet, 'Bloco')
router.register('acelerometro',BlocoAcelerometroViewSet, 'Acelerometro')
router.register('aceleracao',BlocoAceleracaoViewSet, 'Aceleracao')

urlpatterns = [
    #path('api-token-auth/', obtain_auth_token),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
