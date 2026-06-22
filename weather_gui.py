import tkinter as tk
import requests

API_KEY = "c4e3361c30e804b5f630affbf7f8f796"

def get_weather():
    city = city_entry.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        result.config(
            text=f"""
City: {data['name']}

Temperature: {data['main']['temp']} °C

Feels Like: {data['main']['feels_like']} °C

Humidity: {data['main']['humidity']} %

Pressure: {data['main']['pressure']} hPa

Wind Speed: {data['wind']['speed']} m/s

Condition: {data['weather'][0]['description']}
"""
        )
    else:
        result.config(text="City not found!")


root = tk.Tk()
root.title("Real-Time Weather Forecast System")
root.geometry("500x400")


tk.Label(
    root,
    text="Enter City Name",
    font=("Arial", 14, "bold")
).pack(pady=10)


city_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12)
)
city_entry.pack()


tk.Button(
    root,
    text="Get Weather",
    command=get_weather,
    font=("Arial", 12),
    width=15,
    height=1
).pack(pady=15)


result = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    justify="left"
)
result.pack(pady=10)
root.mainloop()