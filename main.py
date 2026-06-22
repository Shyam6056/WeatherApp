import requests

API_KEY = "YOUR_API_KEY"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\n========== WEATHER REPORT ==========")
    print(f"City        : {data['name']}")
    print(f"Temperature : {data['main']['temp']} °C")
    print(f"Feels Like  : {data['main']['feels_like']} °C")
    print(f"Humidity    : {data['main']['humidity']} %")
    print(f"Pressure    : {data['main']['pressure']} hPa")
    print(f"Wind Speed  : {data['wind']['speed']} m/s")
    print(f"Condition   : {data['weather'][0]['description']}")
    print("====================================")
else:
    print("City not found!")