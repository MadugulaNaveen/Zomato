from django.urls import path
from .views import RestaurantDetail, RestaurantList

urlpatterns = [
    path("restaurants/<int:pk>/", RestaurantDetail.as_view(), name="restaurant-detail"),
    path("restaurants/", RestaurantList.as_view(), name="restaurant-list"),
]