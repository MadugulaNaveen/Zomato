from django.shortcuts import render
from rest_framework import generics,filters
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class RestaurantPagination(PageNumberPagination):
  page_size = 9
  page_size_query_param = 'page_size'
  max_page_size = 100
  

class RestaurantDetail(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    pagination_class = RestaurantPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['country_code','cost_for_two']
    search_fields = ['name']
    