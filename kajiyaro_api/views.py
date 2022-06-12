from rest_framework.permissions import AllowAny
from rest_framework import viewsets, generics
from .serializers import CategorySerializer, HouseworkSerializer, TaskSerializer
from .models import Category, Housework, Task

class HouseworkListView(generics.ListAPIView):
    queryset = Housework.objects.all()
    serializer_class = HouseworkSerializer
    permission_classes = (AllowAny,)


class HouseworkRetrieveView(generics.RetrieveAPIView):
    queryset = Housework.objects.all()
    serializer_class = HouseworkSerializer
    permission_classes = (AllowAny,)


class HouseworkViewSet(viewsets.ModelViewSet):
    queryset = Housework.objects.all()
    serializer_class = HouseworkSerializer
    # permission_classes = (AllowAny,)

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (AllowAny,)

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)


class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer