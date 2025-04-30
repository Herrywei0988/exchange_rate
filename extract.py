# extract.py
from prefect import flow, task
from dotenv import load_dotenv
import os, requests, pandas as pd
from datetime import datetime

load_dotenv()
API_KEY = os.getenv("OPEN_EXCHANGE_APP_ID")

@task
def fetch_rates(base='USD'):
    url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}&base={base}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"API failed: {response.status_code}")

    data = response.json()
    rates = data.get("rates", {})
    timestamp = data.get("timestamp", "")

    df = pd.DataFrame([
        {'base': base, 'target': k, 'rate': v, 'timestamp': timestamp}
        for k, v in rates.items()
    ])
    df.to_csv("data/open_exchange_rates.csv", index=False)
    print("CSV updated at", datetime.now())
    return df

@flow(name="Exchange Rate ETL Flow")
def exchange_rate_flow():
    fetch_rates()

if __name__ == "__main__":
    exchange_rate_flow()
