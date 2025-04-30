from prefect import flow, task
from extract import fetch_rates
from validate import validate_data
from transform import transform_data
from load import save_to_csv, save_to_sqlite

@task
def validate_task(df):
    return validate_data(df)

@task
def transform_task(df):
    return transform_data(df)

@task
def load_csv_task(df, filename="data/open_exchange_rates.csv"):
    save_to_csv(df, filename)

@task
def load_sqlite_task(df, db_name="exchange_rates.db", table_name="exchange_rates"):
    save_to_sqlite(df, db_name, table_name)

@flow(name="Exchange Rate ETL Pipeline")
def etl_pipeline(base_currency='USD'):
    df_raw = fetch_rates.fn(base_currency)
    df_validated = validate_task(df_raw)
    df_transformed = transform_task(df_validated)
    load_csv_task(df_transformed)
    load_sqlite_task(df_transformed)

if __name__ == "__main__":
    etl_pipeline()
