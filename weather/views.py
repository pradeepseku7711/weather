import requests,json
from django.shortcuts import render
from .forms import cityForm
from .models import city

# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    
    
    cities = city.objects.all()
    if request.method == 'POST':
        form = cityForm(request.POST)
        form.save()

    
    
    weather_data =[]
    
    try :
        for cityy in cities:
            
            
            r = requests.get(url.format(cityy.name)).json()


            city_weather={
                        'city':cityy.name,
                        'temperature':r['main']['temp'],
                        'description':r['weather'][0]['description'],
                        'icon':r['weather'][0]['icon']

                }
            weather_data.append(city_weather)
        context={'city_weather':weather_data,'cityForm':cityForm()}


    except KeyError:
        context={'city_weather':weather_data,'cityForm':cityForm()}
        
        
        
        
    return render(request,'weather/index.html',context)
