import requests

class APIException(Exception):
    pass

def get_currency_exchange_rate(base_currency, target_currency):

    url = f'https://api.fxratesapi.com/convert?from={base_currency}&to={target_currency}&format=json'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'success' in data:
            if 'info' in data and 'rate' in data['info']:
                exchange_rate_data = data['info']['rate']
                return exchange_rate_data
            else:
                return "Целевая валюта не найдена"
        else:
            return "Неверный формат данных"
    else:
        return "Ошибка при получении данных"


