import json
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


@dataclass
class WeatherData:
    city: str
    temperature: int
    country: str


def load_cities(filepath: str = "Cities.txt") -> list[str]:
    with open(filepath, "r", encoding="utf-8-sig") as f:
        cities = [line.strip() for line in f if line.strip()]
    return list(dict.fromkeys(cities))


def fetch_weather(city: str) -> WeatherData:
    url = f"https://wttr.in/{urllib.parse.quote(city)}?format=j1"
    req = urllib.request.Request(url, headers={"User-Agent": "wttr-weather-aggregator"})
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))

    country = data["nearest_area"][0]["country"][0]["value"]
    temperature = int(data["current_condition"][0]["temp_C"])

    return WeatherData(city=city, temperature=temperature, country=country)


def format_temperature(temp: int) -> str:
    if temp > 0:
        return f"+{temp} °C"
    return f"{temp} °C"


def main():
    cities = load_cities("Cities.txt")
    weather_list = []

    for city in cities:
        try:
            weather = fetch_weather(city)
            weather_list.append(weather)
            print(f"{weather.city}, {weather.country} {format_temperature(weather.temperature)}")
        except Exception as e:
            print(f"Ошибка получения погоды для {city}: {e}")


if __name__ == "__main__":
    main()
