from django.conf.urls import include
from django.db import router
from django.urls import path
from rest_framework import routers
from .views import CategoryViewSet, HouseworkViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'houseworks', HouseworkViewSet, basename='houseworks')

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]