import requests

def get_all_available_currencies():
    url = f'https://api.fxratesapi.com/currencies'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

result = get_all_available_currencies()

if result:
    for currency_code, currency_info in result.items():
        code = currency_info['code']
        name = currency_info['name']
        print(f'Код: {code}, Валюта: {name}')
else:
    print("Ошибка при получении данных")