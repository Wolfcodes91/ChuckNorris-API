from random import choice
from django.shortcuts import render, redirect
import requests

# Create your views here.

def home(request):
    categories = requests.get('https://api.chucknorris.io/jokes/categories').json()
#   get the category from the submitted form

    category = request.GET.get('category')
    if category:
        r = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')
        chuck = r.json()
    else:
        r = requests.get('https://api.chucknorris.io/jokes/random')
        chuck = r.json()
    
    return render(request, 'home.html', {'value': chuck['value'], 'categories': categories})
