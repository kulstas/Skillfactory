# С5.6. Итоговое практическое задание
# Телеграм-бот: Конвертор валют
# Студент: Кулагин Станислав
# Поток: FWP_123

import requests
import json
from config import keys, HEADERS

class ConvertionExeption(Exception):
    pass

class CryptoConvertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExeption(f'Вы указали одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f"Ну удалось обработать количество {amount}")

        url = f'https://api.apilayer.com/currency_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}'
        r = requests.get(url, headers=HEADERS)  # добавляем apikey в заголовок запроса
        total_base = json.loads(r.content)['result']
        print(total_base)

        return total_base