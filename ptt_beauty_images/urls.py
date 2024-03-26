"""ptt_beauty_images URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from images.views import ImageViewSet, Stock6Sign202212ViewSet, Stock6Sign202304ViewSet, Stock6Sign202308ViewSet, Stock6Sign202309ViewSet, Stock6Sign202310ViewSet, Stock6Sign202311ViewSet, Stock6Sign202312ViewSet, Stock6Sign202402ViewSet

router = DefaultRouter()
router.register('images', ImageViewSet)
router.register('Stock6Sign202212', Stock6Sign202212ViewSet)
router.register('Stock6Sign202304', Stock6Sign202304ViewSet)
router.register('Stock6Sign202308', Stock6Sign202308ViewSet)
router.register('Stock6Sign202309', Stock6Sign202309ViewSet)
router.register('Stock6Sign202310', Stock6Sign202310ViewSet)
router.register('Stock6Sign202311', Stock6Sign202311ViewSet)
router.register('Stock6Sign202312', Stock6Sign202312ViewSet)
router.register('Stock6Sign202402', Stock6Sign202402ViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # for rest_framework
    path('api/', include(router.urls)),
    # for rest_framework auth
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
