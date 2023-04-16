import json
import requests
from decouple import config


API_KEY = config('API_KEY')
API_ENDPOINT = 'https://v6.exchangerate-api.com/v6'



def convert_currency(from_currency: str, to_currency: str, amount: float) -> float:
    url = f"{API_ENDPOINT}/{API_KEY}/latest/{from_currency}"
    
    response = requests.get(url)
    currency_data = response.json()
    exchange_rate = currency_data['conversion_rates'][to_currency]
    exchanged_value = exchange_rate * amount
    return exchanged_value

def get_currencies() -> list:
    currency_codes = []
    with open('currency.json') as f:
        currency_data = json.load(f)
        for currency in currency_data:
            code, _ = list(currency.items())[0]
            currency_codes.append(code)
        return sorted(currency_codes)

#print(convert_currency('USD', 'NGN', 1000.0))