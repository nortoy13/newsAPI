from django.urls import path
from .views import NewsView, CategoryView

urlpatterns = [
    path('news/', NewsView.as_view({'get': 'list', 'post': 'create'})),
    path('news/<int:pk>', NewsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('categories/', CategoryView.as_view({'get': 'list', 'post': 'create'})),
    path('categories/<int:pk>', CategoryView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
