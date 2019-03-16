
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import PermissionViewSet, RoleViewSet, UserViewSet, MyTokenObtainPairView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)



router = routers.DefaultRouter();
router.register('permission',PermissionViewSet, 'Permission')
router.register('role',RoleViewSet, 'Role')
router.register('user',UserViewSet,'User')

urlpatterns = [
    #path('api-token-auth/', obtain_auth_token),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
