from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import News, Category
from .serializers import NewsSerializer, CategorySerializer


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminUser,)
    search_fields = ['title', 'content']


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)