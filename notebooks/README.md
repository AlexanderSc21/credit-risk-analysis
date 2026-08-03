# 📓 Notebooks Documentation

> ⚠️ **Note on GitHub Rendering:** GitHub's native viewer occasionally fails to load Jupyter Notebooks or drops their formatting. If any notebook fails to render, **this is a known GitHub issue**. Please use the **nbviewer** links provided below for a guaranteed, clean, and instant view of the code.

This directory contains the sequential Jupyter Notebooks used for the end-to-end processing, validation, and analysis of the credit risk data.

## ⚙️ Execution Order

To understand the data pipeline correctly, the notebooks should be reviewed in the following order:

1. **`01_bronze_to_silver.ipynb` (Cleaning & Null Handling)**
   * **Purpose:** Initial data profiling, strict handling of missing values, and identifying core risk features following Medallion Architecture.

2. **`02_silver_to_gold.ipynb` (Architecture Splitting & Feature Eng)**
   * **Purpose:** Transforms the cleaned data and splits it into BI (hindsight) and ML (foresight) pathways to prevent data leakage.

3. **`03_bi_star_schema.ipynb` (Dimensional Modeling)**
   * **Purpose:** Builds the Star Schema design (Fact and Dimension tables) in DuckDB, optimized for Power BI consumption.

4. **`04_data_validation.ipynb` (Data Quality & Validation)**
   * **Purpose:** Applies strict data quality checks ensuring schema consistency, non-null constraints, and referential integrity.

5. **`05_sql_analysis.ipynb` (SQL Analytics)**
   * **Purpose:** Runs highly optimized analytical SQL queries using DuckDB to extract the key insights displayed in the executive dashboard.

---
*Note: Raw data files are excluded from this directory via `.gitignore` to maintain repository performance.*