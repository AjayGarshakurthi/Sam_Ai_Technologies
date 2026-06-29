import requests

API_KEY = "Yor_weather_API_Key"
def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    print(data) 

    temp = data["main"]["temp"]

    return f"Temperature is {temp} degree Celsius"