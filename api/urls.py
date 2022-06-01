from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import PostViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# Создаем router и регистрируем ViewSet
router = DefaultRouter()

router.register(r'posts', PostViewSet)


urlpatterns = [

    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]