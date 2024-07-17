from django.shortcuts import render
from rest_framework import generics 
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class RestaurantPagination(PageNumberPagination):
  page_size = 10
  page_size_query_param = 'page_size'
  max_page_size = 100
  

class RestaurantDetail(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    pagination_class = RestaurantPagination