from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from hr.views import TaskViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]