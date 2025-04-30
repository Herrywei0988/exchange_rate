import sqlite3


def save_to_csv(df, filename="exchange_rates.csv"):
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


def save_to_sqlite(df, db_name="exchange_rates.db", table_name="exchange_rates"):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Data saved to {db_name} (table: '{table_name}')")


# For testing
if __name__ == "__main__":
    from extract import fetch_exchange_rates
    from validate import validate_data
    from transform import transform_data

    df = fetch_exchange_rates(base_currency="USD", target_currencies=["EUR", "JPY", "TWD"])
    df = validate_data(df)
    df = transform_data(df)

    save_to_csv(df)
    save_to_sqlite(df)