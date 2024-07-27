from django.shortcuts import render
import requests
from .countries import data_dict
import random

def restaurant_list(request):
    page = request.GET.get('page', 1)
    country = request.GET.get('country', '')
    cost_for_two = request.GET.get('cost_for_two','')
    search = request.GET.get('search','')
    
    countries = data_dict.keys()
    country_code = data_dict.get(country)

    params = {
        'page': page,
        'country_code': country_code,
        'cost_for_two': cost_for_two,
        'search': search,
    }

    try:
        response = requests.get('http://127.0.0.1:8000/api/restaurants/', params=params)
        response.raise_for_status()
        data = response.json()
        restaurants = data['results']
        pagination = {
            'count': data['count'],
            'next': data['next'],
            'previous': data['previous'],
            'current_page': int(page),
            'total_pages': (data['count'] // 9) + (1 if data['count'] % 9 else 0)
        }
    except requests.exceptions.RequestException as e:
        restaurants = []
        pagination = {}
        error = str(e)

    return render(request, 'restaurant_list.html', {
        'restaurants': restaurants,
        'pagination': pagination,
        'country_code': country_code,
        'cost_for_two': cost_for_two,
        'search':search,
        'countries':countries,
        'selected_country':country,
    })

def restaurant_detail(request,id):
  response = requests.get(f'http://127.0.0.1:8000/api/restaurants/{id}/')
  restaurant = response.json()
  reverse_country_mapping = {v: k for k, v in data_dict.items()}
  restaurant['country'] = reverse_country_mapping.get(restaurant['country_code'])
  return render(request,'restaurant_detail.html',{'restaurant':restaurant})

def random_restaurant(request):
    n = random.randint(1,9000)
    response = requests.get(f'http://127.0.0.1:8000/api/restaurants/{n}/')
    restaurant = response.json()
    reverse_country_mapping = {v: k for k, v in data_dict.items()}
    restaurant['country'] = reverse_country_mapping.get(restaurant['country_code'])
    return render(request,'restaurant_detail.html',{'restaurant':restaurant})
