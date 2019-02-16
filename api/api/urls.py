
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import PermissionViewSet, RoleViewSet, UserViewSet

router = routers.DefaultRouter();
router.register('permission',PermissionViewSet, 'Permission')
router.register('role',RoleViewSet, 'Role')
router.register('user',UserViewSet,'User')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]