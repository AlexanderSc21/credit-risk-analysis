# Project Context: Lending Club Credit Risk Analysis

## 1. Business Objective
The goal of this project is to analyze the factors that lead to loan defaults (loans in "Charged Off" status) using the public Lending Club dataset. The analysis evaluates risk factors such as FICO scores, Annual Income, Loan Purpose, and Lending Club Sub-Grades to understand risk profiles and default rates.

## 2. Technical Stack
- **Languages:** Python, SQL
- **Database / Compute Engine:** DuckDB (In-memory / Parquet backend)
- **Data Engineering:** Pandas, DuckDB relational queries
- **Visualization:** Matplotlib, Seaborn, Power BI
- **Architecture:** Medallion Architecture (Bronze -> Silver -> Gold -> BI)

## 3. Data Pipeline Architecture (Medallion)

### Bronze to Silver (`01_bronze_to_silver.ipynb`)
- **Action:** Read raw CSV data and perform initial cleaning.
- **Transformations:** 
  - Standardized datetime columns.
  - Stripped formatting characters (e.g., `%`, `months`) and cast to numeric types.
  - Handled missing values (`NaN`) across numerical and categorical columns.

### Silver to Gold (`02_silver_to_gold.ipynb`)
- **Action:** Feature Engineering and strict Data Leakage prevention.
- **The Great Purge:** Removed highly granular credit bureau features (e.g., inquiries in the last 6 months, open accounts, revolving balances) that act as "data leakage". We are predicting risk at the *time of origination*, so we only keep features available before the loan was funded.
- **Feature Engineering:**
  - Consolidated `fico_range_low` and `fico_range_high` into a single `fico_score`.
  - Calculated credit history length in years using vectorized Pandas `DateOffset` logic for sub-second performance.
  - Created categorical bins for annual income and FICO scores.

### Gold to BI Star Schema (`03_bi_star_schema.ipynb`)
- **Action:** Transitioned from a flat analytical table to a Star Schema optimized for Power BI.
- **Why?** To prevent UI lag in Power BI and offload heavy DAX computations to DuckDB.
- **Dimensions:**
  - `dim_date`: Pre-computed year, quarter, and month names to avoid heavy Power BI Auto Date/Time overhead.
  - `dim_risk`: Mapped numeric LC grades to clean string labels.
  - `dim_geography`: Translated 2-letter state codes to fully qualified names (e.g. `MS` -> `Mississippi, USA`) for Azure Maps.
  - `dim_purpose`: Standardized loan purposes.
- **Fact Table:** `fact_loans` retaining all ~50 analytical features and computed business-logic columns.

## 4. Validations & BI Integration

### Dashboard Mirror Tests (`04_data_validation.ipynb`)
Automated SQL tests to validate that the DuckDB data perfectly aligns with the Power BI dashboard KPIs.
- Verified row counts (2.25M) and Primary Key uniqueness.
- Reproduced the Global Default Rate (21.23%).
- Replicated complex geographic and income-bucket aggregations exactly as they appear in the UI.

### Production-Ready SQL Analysis (`05_sql_analysis.ipynb` & `scripts/generate_sql_reports.py`)
Exploratory SQL analysis using a **Dual-Environment Strategy**:
1. **Interactive Notebook:** `05_sql_analysis.ipynb` uses `plt.show()` for human readability, code reviews, and portfolio presentation.
2. **Headless Automation:** `scripts/generate_sql_reports.py` uses the Matplotlib `Agg` backend and `plt.close()`. This "Production-Ready" script can run autonomously on cloud servers (AWS/Azure) or via Airflow without crashing due to missing graphical displays.

> **Crucial Business Logic (Default Rate Filtering):** 
> The BI dataset contains over 1 million "Current" (active) loans to provide realistic volume for the dashboard. However, active loans have an unknown outcome (`default_flag IS NULL`). To avoid artificially diluting the risk metrics, all SQL analysis strictly filters `WHERE default_flag IS NOT NULL` to evaluate default rates solely on loans that have completed their lifecycle.
