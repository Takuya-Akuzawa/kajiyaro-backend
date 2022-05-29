from django.conf.urls import include
from django.db import router
from django.urls import path
from rest_framework import routers
from .views import HouseworkViewSet, HouseworkListView, HouseworkRetrieveView, \
                    CategoryViewSet, CategoryListView, CategoryRetrieveView

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'houseworks', HouseworkViewSet, basename='houseworks')

urlpatterns = [
    path('list-housework/', HouseworkListView.as_view(), name='list-housework'),
    path('detail-housework/<str:pk>/', HouseworkRetrieveView.as_view(), name='detail-housework'),
    
    path('list-category/', CategoryListView.as_view(), name='list-category'),
    path('detail-category/<str:pk>/', CategoryRetrieveView.as_view(), name='detail-category'),
    
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]