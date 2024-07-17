from django.shortcuts import render
import requests

# Create your views here.
def restaurant_list(request):
    # Get the page number from the request, default to 1
    page = request.GET.get('page', 1)
    
    # Make a request to the API with the page parameter
    response = requests.get(f'http://127.0.0.1:8000/api/restaurants/', params={'page': page})
    data = response.json()
    
    restaurants = data['results']
    pagination = {
        'count': data['count'],
        'next': data['next'],
        'previous': data['previous'],
        'current_page': page,
        'total_pages': (data['count'] // 10) + (1 if data['count'] % 10 else 0)
    }
    
    return render(request, 'restaurant_list.html', {'restaurants': restaurants, 'pagination': pagination})



def restaurant_detail(request,id):
  response = requests.get(f'http://127.0.0.1:8000/api/restaurants/{id}/')
  restaurant = response.json()
  return render(request,'restaurant_detail.html',{'restaurant':restaurant})

