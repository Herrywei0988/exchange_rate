# Exchange Rate ETL Pipeline

This project is an **ETL (Extract, Transform, Load)** pipeline built with Python and Prefect to automate the retrieval, validation, transformation, and storage of foreign exchange rate data.

## 📌 Features
- Extract exchange rate data using the [exchangerate.host](https://exchangerate.host) API
- Validate data schema using **Pandera**
- Transform data (e.g., rounding, date parsing)
- Save to both **CSV** and **SQLite** formats
- Orchestrate with **Prefect** and deploy to **Prefect Cloud**
- Scheduled to run **every hour** using a cron job

---

## 🗂️ Project Structure
```text
exchange_rate/
├── extract.py          # Download exchange rates from exchangerate.host
├── transform.py        # Clean and format the extracted data
├── validate.py         # Schema validation with Pandera
├── load.py             # Save to CSV and SQLite database
├── pipeline.py         # Prefect pipeline definition
├── prefect.yaml        # Saved deployment configuration
├── requirements.txt    # Dependencies
└── README.md           # Project overview and instructions
```

---

## ⚙️ Installation
```bash
# Clone the repo
git clone <this-repo>
cd exchange_rate

# Create and activate virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 How to Run Locally (Manual Run)
```bash
python extract.py      # Test extraction
python validate.py     # Test validation
python transform.py    # Test transformation
python load.py         # Save as CSV and SQLite
```

---

## 🧠 Run with Prefect
### 1. Authenticate with Prefect Cloud
```bash
prefect cloud login
```

### 2. Deploy the pipeline
```bash
prefect deploy pipeline.py:etl_pipeline \
  --name "Exchange Rate ETL" \
  --cron "0 * * * *"  # every hour
```
Follow the prompts to select:
- Work pool: `local-pool`
- Storage: **No** remote storage

### 3. Start your worker
```bash
prefect worker start --pool local-pool
```

### 4. Trigger a manual run
```bash
prefect deployment run "Exchange Rate ETL Pipeline/Exchange Rate ETL"
```

### 5. Monitor on Prefect Cloud
Go to:
```
https://app.prefect.cloud
```
And log in to see:
- Flows
- Executions
- Logs

---

## 📁 Output
- `exchange_rates.csv`  → Cleaned data in CSV format
- `exchange_rates.db`   → SQLite database table `exchange_rates`

---

## 📦 Dependencies
```
pandas
requests
pandera>=0.17.0
prefect>=3.0
sqlite3 (built-in)
```

---

## 🧾 License
This project is for educational purposes as part of a Data Structures & Algorithms course.

---

## 🙋‍♂️ Author
**Herry Wei**
Graduate Student, Georgetown University

---

## ✅ To Do
- [ ] Add unit tests
- [ ] Dockerize the pipeline (optional)
- [ ] Add email/Slack notification integration with Prefect

