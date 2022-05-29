from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializers import CategorySerializer, HouseworkSerializer
from .models import Category, Housework


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (AllowAny,)


class HouseworkViewSet(viewsets.ModelViewSet):
    queryset = Housework.objects.all()
    serializer_class = HouseworkSerializer
    # permission_classes = (AllowAny,)
