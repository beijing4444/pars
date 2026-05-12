import requests
from bs4 import BeautifulSoup


URL = "https://www.gismeteo.ru/weather-moscow-4368/10-days/"


def ckahatstr(url):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers,)
    response.raise_for_status()

    return response.text


def parse_pogod(html):

    soup = BeautifulSoup(html, "lxml")

    dates = soup.select(".widget-row-days-date .date")
    temperatures = soup.select(".widget-row-chart-temperature .unit_temperature_c")
    descriptions = soup.select(".widget-row-icon .tooltip")

    weather = []

def main():
    html = ckahatstr(URL)
    forecast = parse_pogod(html)

    if not forecast:
        print("Не получилось найти погоду.")
        return

    print("Погода на 5 дней:")
    print("-" * 30)

    for item in forecast:
        print(f"День: {item['day']}")
        print(f"Температура: {item['temperature']}")
        print(f"Описание: {item['description']}")
        print("-" * 30)


if __name__ == "__main__":
    main()