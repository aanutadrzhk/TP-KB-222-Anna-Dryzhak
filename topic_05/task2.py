import requests

def get_exchange_rate(currency_code):
    response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json")
    data = response.json()
    return data[0]['rate'] if data else None

def convert_currency(amount, from_currency):
    from_rate = get_exchange_rate(from_currency)

    if from_rate is None:
        return None

    converted_amount = amount * from_rate
    return converted_amount

def main():
    print("Конвертер валют: EUR, USD, PLN в UAH")
    amount = float(input("Введіть суму: "))
    from_currency = input("Введіть валюту (EUR, USD, PLN): ").upper()

    result = convert_currency(amount, from_currency)
    if result is not None:
        print(f"{amount} {from_currency} = {result} UAH")
    else:
        print("Не вдалося отримати курси валют. Спробуйте пізніше.")

if __name__ == "__main__":
    main()
