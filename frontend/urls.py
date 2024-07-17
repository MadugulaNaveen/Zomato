from django.urls import path
from .views import restaurant_list, restaurant_detail

urlpatterns = [
    path('', restaurant_list, name='restaurant-list'),
    path('<int:id>/', restaurant_detail, name='restaurant-detail'),
]
