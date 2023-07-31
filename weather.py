import requests


cities = ['Лондон', 'Аэропорт Шереметьево', 'Череповец']
payload = {'nmMTq': '',  # тут все нужные параметры отображения и едениц измерений
           'lang': 'ru'}
for city in cities:
    url = f'https://wttr.in/{city}'
    response = requests.get(url, params=payload)  # params ставит '=' даже когда нет значения, но это ни на что не влияет
    response.raise_for_status()

    print(response.text)
