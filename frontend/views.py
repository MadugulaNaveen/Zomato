from django.shortcuts import render
import requests
from .countries import data_dict
from django.conf import settings
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
        response = requests.get('settings.API_BASE_URL', params=params)
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
    api_url = f"{settings.API_BASE_URL}{id}/"
    response = requests.get(api_url)
    restaurant = response.json()
    reverse_country_mapping = {v: k for k, v in data_dict.items()}
    restaurant['country'] = reverse_country_mapping.get(restaurant['country_code'])
    return render(request,'restaurant_detail.html',{'restaurant':restaurant})

def random_restaurant(request):
    n = random.randint(1,9000)
    api_url = f"{settings.API_BASE_URL}{n}/"
    response = requests.get(api_url)
    restaurant = response.json()
    reverse_country_mapping = {v: k for k, v in data_dict.items()}
    restaurant['country'] = reverse_country_mapping.get(restaurant['country_code'])
    return render(request,'restaurant_detail.html',{'restaurant':restaurant})
