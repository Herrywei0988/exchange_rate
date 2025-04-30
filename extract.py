import requests
import pandas as pd


def fetch_exchange_rates(base_currency='USD', target_currencies=None):
    if target_currencies:
        symbols_param = ','.join(target_currencies)
        url = f"https://api.exchangerate.host/latest?base={base_currency}&symbols={symbols_param}"
    else:
        url = f"https://api.exchangerate.host/latest?base={base_currency}"

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")

    data = response.json()

    # Extract fields
    rates = data.get('rates', {})
    date = data.get('date', '')

    df = pd.DataFrame({
        'base': base_currency,
        'target': list(rates.keys()),
        'rate': list(rates.values()),
        'date': date
    })

    return df


# For testing
if __name__ == "__main__":
    df = fetch_exchange_rates(base_currency='USD', target_currencies=['EUR', 'JPY', 'TWD'])
    print(df)
