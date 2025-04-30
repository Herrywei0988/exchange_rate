import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("data/open_exchange_rates.csv")

    # Convert timestamp to readable datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s").dt.date

    # Get all unique currencies from base and target columns
    currencies = sorted(set(df["base"].unique()).union(df["target"].unique()))

    # Show only the first 40 rows as preview table
    table_html = df.head(40).to_html(classes="table table-striped table-bordered table-hover", index=False)

    return render_template("index.html", currencies=currencies, table=table_html)


@app.route("/convert")
def convert():
    base = request.args.get("from")
    target = request.args.get("to")
    amount = float(request.args.get("amount", 0))

    df = pd.read_csv("data/open_exchange_rates.csv")

    # Find the exchange rate for the specified base and target
    row = df[(df["base"] == base) & (df["target"] == target)]

    if row.empty:
        return jsonify({"error": "Rate not found"}), 404

    rate = float(row["rate"].values[0])
    result = amount * rate

    return jsonify({
        "rate": round(rate, 4),
        "converted_amount": round(result, 2)
    })


if __name__ == "__main__":
    app.run(debug=True)
