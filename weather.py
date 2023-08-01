import requests


def weather_report():
    """
    This function retrieves weather information for each city in the 'cities' list using the wttr.in service,
    and prints the weather report in the console.
    """
    cities = ['Лондон', 'Аэропорт Шереметьево', 'Череповец']
    payload = {'nmMTq': '',
               'lang': 'ru'}
    for city in cities:
        url = f'https://wttr.in/{city}'

        response = requests.get(url, params=payload)
        response.raise_for_status()

        print(response.text)


if __name__ == '__main__':
    weather_report()
