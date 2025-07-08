import tkinter as tk
import requests

API_KEY = "bd5e378503939ddaee76f12ad7a97608"

def get_weather():
    city = city_entry.get().strip()
    if not city:
        result_label.config(text="⚠️ Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        res = requests.get(url)
        data = res.json()

        if res.status_code == 200:
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"].capitalize()
            result = f"🌍 {city.title()}\n🌡️ {temp}°C\n🌤️ {weather}"
            result_label.config(text=result)
        else:
            result_label.config(text="❌ City not found")
    except Exception as e:
        result_label.config(text="⚠️ Error connecting to API")

# GUI setup
root = tk.Tk()
root.title("Simple Weather App")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Enter City:", font=("Arial", 12)).pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), justify="center")
result_label.pack(pady=20)

root.mainloop()
