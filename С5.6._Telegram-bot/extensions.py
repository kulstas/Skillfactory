# С5.6. Итоговое практическое задание
# Телеграм-бот: Конвертор валют
# Студент: Кулагин Станислав
# Поток: FWP_123

import requests
import json
from config import keys, HEADERS

class APIException(Exception):
    pass

class CryptoConvertor:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Вы указали одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Ну удалось обработать количество {amount}")

        url = f'https://api.apilayer.com/currency_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}'
        r = requests.get(url, headers=HEADERS)  # добавляем apikey в заголовок запроса
        total_base = json.loads(r.content)['result']

        return total_base