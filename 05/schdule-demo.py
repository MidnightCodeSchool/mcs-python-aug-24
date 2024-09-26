"""
poetry add schedule httpx
"""
import httpx
from rich import print
import schedule
from time import sleep

def get_weather():
    city = "Tokyo"
    API_KEY = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    r = httpx.get(url)
    feels_like = r.json()["main"]["feels_like"]
    print(f"Feels like: {feels_like}")
    return  feels_like

schedule.every(10).seconds.do(get_weather)

while True:
    schedule.run_pending()
    sleep(1)