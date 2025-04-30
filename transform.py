import pandas as pd


def transform_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df['rate'] = df['rate'].round(4)
    return df


# For testing
if __name__ == "__main__":
    from extract import fetch_exchange_rates
    from validate import validate_data

    df = fetch_exchange_rates(base_currency='USD', target_currencies=['EUR', 'JPY', 'TWD'])
    df = validate_data(df)
    df = transform_data(df)
    print(df)