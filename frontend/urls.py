from django.urls import path
from .views import restaurant_list, restaurant_detail,random_restaurant

urlpatterns = [
    path('', restaurant_list, name='restaurant-list'),
    path('<int:id>/', restaurant_detail, name='restaurant-detail'),
    path('random',random_restaurant,name='random_restaurant'),
]
