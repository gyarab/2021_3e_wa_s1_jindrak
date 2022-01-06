import httpx
from pprint import pprint

# nacist vstupy
input_value = float(input("Zadejte hodnotu k prevedeni: "))
target_currency = input("Zadejte cilovou menu: ")

#stahnout data
r = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt')
rates_str = r.text

target_rate_str = None
rates_list = rates_str.split('\n')
for rate_item in rates_list:
    if target_currency in rate_item:
        # ulozit target_rate
        target_rate_str = rate_item

rate = float(target_rate_str.split('|')[-1].replace(',', '.'))

# vypocet

output_value = input_value / rate

# vystup

print(f"Prevedena castka: {output_value:.2f} {target_currency}")
#pprint(rates_list)273