import json
import requests
from decouple import config


API_KEY = config('API_KEY')
API_ENDPOINT = 'https://v6.exchangerate-api.com/v6'
url = f"{API_ENDPOINT}/{API_KEY}/latest"

response = requests.get(url)

currency_data = response.json()

#print(currency_data)
output = json.dumps(currency_data, indent = 4)
outp = sorted(output)
with open('output.json', 'w', encoding='utf-8') as a:
    a.write(sorted(outp))
    

    #exchange_rate = currency_data['data'][to_currency]['value']
    #exchanged_value = exchange_rate * amount
    #return exchanged_value
