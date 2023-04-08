import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(reguest):
    appid = '8b78cb6da2d98c5f2540773af280dca0'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if(reguest.method == 'POST'):
        form = CityForm(reguest.POST)
        form.save()

    form = CityForm()
    
    cities = City.objects.all()

    all_cities = []
    for city in cities:
        response = requests.get(url.format(city))
        if response.status_code == 404:
            continue
        city_weather = response.json()
        res = requests.get(url.format(city.name)). json()
        # print()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res["weather"][0]["icon"]
        } 
        
    all_cities.append(city_info)
        
    context = {'all_info': all_cities, 'form': form}

    return render(reguest, 'weather/index.html', context)

    
