# Credit Risk Analysis
> Loan default risk analysis using Python, SQL and Power BI

## Overview
Analysis of LendingClub loan data (2007-2018) to identify credit risk patterns and default behavior across 1.2M+ loans.

## Stack
- **Python / Pandas** — ETL and EDA
- **DuckDB** — SQL analytics
- **Power BI** — Dashboard

## Architecture
Raw Data (Bronze) → Cleaned Data (Silver) → Star Schema (Gold) → Power BI

## Dataset
Source: [LendingClub Loan Data — Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club)  
Size: 2.2M loans | 151 columns | 2007–2018

## Structure
/data/bronze → raw data  
/data/silver → cleaned data  
/data/gold → dimensional model  
/notebooks → EDA and ETL  
/sql → analytical queries  
/dashboard → Power BI file  
/images → dashboard screenshots  

## Author
Alexander Sinte — [GitHub](https://github.com/AlexanderSc21)