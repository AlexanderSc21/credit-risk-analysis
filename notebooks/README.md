# 📓 Notebooks Documentation

> ⚠️ **Note on GitHub Rendering:** GitHub's native viewer occasionally fails to load Jupyter Notebooks or drops their formatting. If any notebook fails to render, **this is a known GitHub issue**. Please use the **nbviewer** links provided below for a guaranteed, clean, and instant view of the code.

This directory contains the sequential Jupyter Notebooks used for the end-to-end processing, validation, and analysis of the credit risk data.

## ⚙️ Execution Order

To understand the data pipeline correctly, the notebooks should be reviewed in the following order:

1. **`01_eda.ipynb` (Exploratory Data Analysis)**
   * **Purpose:** Initial data profiling, handling missing values, and identifying core risk features.
   * [View Online via nbviewer](https://nbviewer.org/github/AlexanderSc21/credit-risk-analysis/blob/main/notebooks/01_eda.ipynb)

2. **`02_gold.ipynb` (Dimensional Modeling)**
   * **Purpose:** Transforms the cleaned data into a Star Schema design (Fact and Dimension tables) ready for analytical querying.
   * [View Online via nbviewer](https://nbviewer.org/github/AlexanderSc21/credit-risk-analysis/blob/main/notebooks/02_gold.ipynb)

3. **`03_data_validation.ipynb` (Data Quality & Validation)**
   * **Purpose:** Applies data quality checks ensuring schema consistency, non-null constraints, and logical bounds across the pipeline.
   * [View Online via nbviewer](https://nbviewer.org/github/AlexanderSc21/credit-risk-analysis/blob/main/notebooks/03_data_validation.ipynb)

4. **`04_sql_analysis.ipynb` (SQL Analytics with DuckDB)**
   * **Purpose:** Runs highly optimized analytical SQL queries using DuckDB to extract the key insights displayed in the executive dashboard.
   * [View Online via nbviewer](https://nbviewer.org/github/AlexanderSc21/credit-risk-analysis/blob/main/notebooks/04_sql_analysis.ipynb)

---
*Note: Raw data files are excluded from this directory via `.gitignore` to maintain repository performance.*