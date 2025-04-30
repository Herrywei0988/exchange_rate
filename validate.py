import pandera as pa
from pandera import Column, DataFrameSchema, Check


# Define schema for exchange rate DataFrame
exchange_schema = DataFrameSchema({
    "base": Column(str),
    "target": Column(str),
    "rate": Column(float, Check.greater_than(0)),  # rate should be positive
    "date": Column(str)
})


def validate_data(df):
    return exchange_schema.validate(df)


# For testing
if __name__ == "__main__":
    from extract import fetch_exchange_rates
    df = fetch_exchange_rates(base_currency="USD", target_currencies=["EUR", "JPY", "TWD"])
    validated_df = validate_data(df)
    print(validated_df)