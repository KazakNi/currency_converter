import requests
import sys


def get_exchange_rate(currency: str) -> dict:
    try:
        url = f'http://www.floatrates.com/daily/{currency}.json'
        r = requests.get(url)
        return r.json()
    except Exception as e:
        print(f'Error in connection: {e}')


def get_exchange_money(money: float, currency_rate: float|int) -> float:
    return money * currency_rate


def calculation(exchange_currency, cache, user_currency_value, user_currency) -> None:
    if exchange_currency in cache:
        print('Oh! It is in the cache!')
        exchange_rate = cache[exchange_currency]
        print(f'You received {get_exchange_money(user_currency_value, exchange_rate):.2f} {exchange_currency}.')
    else:
        print('Sorry, but it is not in the cache!')
        exchange_rate = get_exchange_rate(user_currency)[exchange_currency]['rate']
        cache[exchange_currency] = exchange_rate
        print(f'You received {get_exchange_money(user_currency_value, exchange_rate):.2f} {exchange_currency}.')


def main() -> None:
    cache = {}
    user_currency = input('Введите код имеющейся валюты')
    exchange_currency = input('Введите валюту продажи')
    try:
        user_currency_value = float(input('Введите сумму Вашей валюты'))
    except Exception as e:
        print(f'Error while input {e}')
    cache['eur'] = get_exchange_rate(user_currency)['eur']['rate']
    if user_currency != 'usd':
        cache['usd'] = get_exchange_rate(user_currency)['usd']['rate']
    first_stage = True
    while True:
        if first_stage:
            print('Checking the cache...')
            calculation(exchange_currency, cache, user_currency_value, user_currency)
            first_stage = False
        else:
            exchange_currency = input()
            if exchange_currency == '':
                sys.exit("No currency input")
            user_currency_value = float(input())
            print('Checking the cache...')
            calculation(exchange_currency, cache, user_currency_value, user_currency)


if __name__ == '__main__':
    main()
