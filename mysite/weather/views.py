from django.shortcuts import render
import requests

API_KEY = "348fc844a5c65f0f5f168bf98c169576"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        return {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "clouds": data["clouds"]["all"],
            "wind": data["wind"]["speed"],
            "error": ""
        }
    except:
        return {"error": "Город не найден"}

def index(request):
    return render(request, "index.html")

def cityweather(request):
    if request.method == "POST":
        city = request.POST.get("cityweather")
        weather = get_weather(city)
        return render(request, "index.html", {"weather": weather})
    
    return render(request, "index.html")