# Fake Store API ETL Pipeline

A simple Python ETL pipeline that extracts product and user data from the Fake Store API, cleans it, and loads it into a local PostgreSQL database.

## 🛠️ Requirements & Tech Stack
- Python 3.x
- PostgreSQL & DBeaver
- Python packages: `pandas`, `requests`, `sqlalchemy`, `psycopg[binary]`

## 📁 Project Structure
- `extract.py`: Fetches raw JSON data from the Fake Store API.
- `transform.py`: Cleans and formats the data using Pandas.
- `load.py`: Connects to PostgreSQL via SQLAlchemy and inserts the data.
- `main.py`: Runs the complete pipeline.

## 🚀 How to Run

1. **Clone the project & set up a virtual environment:**
   ```bash
   git clone https://github.com/Omuricelove/fake-store-etl-pipeline.git
   cd fake-store-etl-pipeline
   python -m venv venv