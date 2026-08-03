# Credit Risk Analysis
> Loan default risk analysis using Python, SQL (DuckDB), and Power BI.

**Project Progress:** ▓▓▓▓▓▓▓▓▓▓ **100% Complete**

## 🚀 Current Status / Roadmap
*This project is complete. Core pipelines are built, and the comprehensive Power BI executive dashboard is live and audited.*

- [x] **Phase 1:** Data Extraction and Initial Cleaning (Python/Pandas)
- [x] **Phase 2:** Dimensional Modeling (Bronze → Silver → Gold Architecture)
- [x] **Phase 3:** Exploratory Data Analysis & SQL Analytics (DuckDB)
- [x] **Phase 4:** Power BI Dashboard Implementation (Executive Summary & Customer Analysis)
- [x] **Phase 5:** Final Dashboard Views (Risk Deep-Dive & Geographic Analysis) and Final Audit

---

## 📈 Dashboard Preview

### Power BI Report Pages
![Executive Summary](images/Page%201%20%28Executive%20Summary%29.png)
![Risk Analysis](images/Page%202%20%28Risk%20Analysis%29.png)
![Customer Analysis](images/Page%203%20%28Customer%20Analysis%29.png)
![Geographic Analysis](images/Page%204%20%28Geographic%20Analysis%29.png)

--- 

## 📊 Key Insights (SQL Analytics)
Based on the analytical queries performed on the processed data, several critical risk patterns have been identified:

* **Credit Grades as Predictors:** Loan grades assigned by LendingClub are strong predictors of default. Grade A loans show a default rate below 5%, while Grade G loans exceed 55% — an 11x difference.
* **Risk by Loan Purpose:** Small business loans show the highest default rate, significantly above the 21.23% average — nearly double compared to lower-risk categories like wedding or car loans.
* **Geographical Concentration:** Mississippi (MS) shows the highest default rate at ~28%, followed by Nebraska (NE) and Arkansas (AR). Southern and Midwestern states tend to concentrate higher credit risk.
* **Temporal Trends & Truncation:** Default rates show a steady increase from 2012 to 2016, peaking above 26% in 2016-Q2 and 2016-Q3. The drop in 2018-Q4 is likely due to data truncation — recent loans haven't reached their final status yet.
* **Income-Default Correlation:** There is a clear inverse relationship between income and default rate. Low-income borrowers (<$40k) default at 25.4%, while very high-income borrowers (>$120k) default at only 16.8% — suggesting income is a strong predictor of repayment capacity.
* **Verification Paradox:** Counterintuitively, "Verified" incomes show higher default rates (25%) than "Not Verified" (15.9%). This is explained by a selection bias (LendingClub likely requested verification for riskier profiles with lower FICO scores).
* **Employment Length Myth:** Contrary to traditional assumptions, the years of employment have virtually zero predictive power on default rates in this portfolio, remaining flat at ~21% across all tenures.

---

## 📖 Overview
Analysis of LendingClub loan data (2007-2018) to identify credit risk patterns and default behavior across 2.2M+ loans.

## 🛠 Stack
- **Python / Pandas** — ETL (Extract, Transform, Load) and EDA
- **DuckDB** — Fast analytical SQL processing
- **Power BI** — Interactive Dashboarding

## 🏗 Architecture
**Data Lakehouse Approach:** Raw Data (Bronze) → Cleaned Data (Silver) → Star Schema (Gold) → Power BI

## 📂 Dataset
* **Source:** [LendingClub Loan Data — Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club)  
* **Size:** 2.2M loans | 151 columns  
* **Timeframe:** 2007–2018  

## 📁 Repository Structure

    ├── data/
    │   ├── bronze/     # Raw, unprocessed data
    │   ├── silver/     # Cleaned and filtered data
    │   └── gold/       # Dimensional model ready for BI (DuckDB)
    ├── notebooks/      # Jupyter notebooks for ETL and validation
    ├── dashboard/      # Power BI template (.pbit)
    ├── scripts/        # Data quality observability
    └── images/         # Dashboard screenshots

---

## 📓 Notebooks (View Online)
If GitHub's native viewer is having trouble rendering the notebooks, you can view them instantly here:

* [01. Bronze to Silver (Cleaning)](https://nbviewer.org/github/AlexanderSc21/credit-risk-analysis/blob/main/notebooks/01_bronze_to_silver.ipynb)
* [02. Silver to Gold (Feature Eng)](https://nbviewer.org/github/AlexanderSc21/credit-risk-analysis/blob/main/notebooks/02_silver_to_gold.ipynb)
* [03. BI Star Schema](https://nbviewer.org/github/AlexanderSc21/credit-risk-analysis/blob/main/notebooks/03_bi_star_schema.ipynb)
* [04. Data Validation](https://nbviewer.org/github/AlexanderSc21/credit-risk-analysis/blob/main/notebooks/04_data_validation.ipynb)
* [05. SQL Analytics](https://nbviewer.org/github/AlexanderSc21/credit-risk-analysis/blob/main/notebooks/05_sql_analysis.ipynb)

---
**Author:** Alexander Sinte — [GitHub](https://github.com/AlexanderSc21)