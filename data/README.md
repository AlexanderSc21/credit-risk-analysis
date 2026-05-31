# 📂 Data Directory

> **Note:** The actual data files (`.csv`, `.parquet`, `.duckdb`) are intentionally excluded from this repository via `.gitignore`. This is a standard best practice to avoid pushing large datasets (2.2M+ records) to GitHub.

## 🏗️ Architecture (Medallion)
This folder is structured following a Data Lakehouse approach:
* **`bronze/`**: Contains the raw, unprocessed data exactly as downloaded from the source.
* **`silver/`**: Contains the cleaned, filtered, and transformed data.
* **`gold/`**: Contains the final Dimensional Model (Star Schema) and the DuckDB database ready for Power BI consumption.

## 🚀 How to Replicate
To run the pipelines locally and generate the database, you must first populate the `bronze` layer. You have two options:

### Option A: Automated Download (Recommended)
If you have your Kaggle API credentials configured, you can use the extraction script:
1. Ensure your `.env` file is set up with your `KAGGLE_TOKEN`.
2. Run the extraction script to fetch the data directly via API:
   ```bash
   python download_data.py
   ```

### Option B: Manual Download
1. Download the raw dataset directly from [Kaggle - LendingClub Loan Data](https://www.kaggle.com/datasets/wordsforthewise/lending-club).
2. Extract the `.zip` file and place the CSVs inside the `data/bronze/` directory.

### Next Steps
Once the raw data is in place, run the notebooks in the `notebooks/` directory in sequential order to build the Silver and Gold layers.