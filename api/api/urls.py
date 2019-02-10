
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import PermissionViewSet, RoleViewSet, UserViewSet

router = routers.DefaultRouter();
router.register('permission',PermissionViewSet)
router.register('role',RoleViewSet)
router.register('user',UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
