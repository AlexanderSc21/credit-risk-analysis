-- =============================================
-- Credit Risk Analysis - KPI Queries
-- Author: Alexander Sinte
-- =============================================

-- 1. Overall default rate

SELECT
    COUNT(*) AS total_loans,
    SUM(default_flag) AS total_defaults,
    ROUND(AVG(default_flag) * 100, 2) AS default_rate_pct,
    ROUND(SUM(funded_amnt), 2) AS total_funded,
    ROUND(AVG(funded_amnt), 2) AS avg_loan_amount,
    ROUND(AVG(int_rate), 2) AS avg_interest_rate
FROM fact_loans;