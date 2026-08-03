import duckdb
import logging
import os
from datetime import datetime

def setup_logger():
    # Set up logging to output to both console and a log file in the same directory
    log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data_quality.log')
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def main():
    logger = setup_logger()
    logger.info("Starting Data Quality Observability Checks...")
    
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'gold', 'goldBI.duckdb')
    
    if not os.path.exists(db_path):
        logger.error(f"Database not found at {db_path}. Pipeline might have failed.")
        return

    try:
        con = duckdb.connect(db_path)
        logger.info("Connected to goldBI.duckdb successfully.")
        
        errors_found = 0
        
        # 1. Check if fact table has data
        row_count = con.execute("SELECT COUNT(*) FROM fact_loans").fetchone()[0]
        if row_count == 0:
            logger.error("Data Quality Exception: fact_loans table is completely empty.")
            errors_found += 1
        else:
            logger.info(f"PASS: fact_loans contains {row_count:,} records.")

        # 2. Check for Ongoing Loans (NULL default_flag)
        null_defaults = con.execute("SELECT COUNT(*) FROM fact_loans WHERE default_flag IS NULL").fetchone()[0]
        logger.info(f"BUSINESS LOGIC: Found {null_defaults:,} ongoing/current loans (default_flag = NULL).")
        if null_defaults == 0:
            logger.warning("Alert: 0 ongoing loans found. This is unusual for the full LendingClub dataset.")

        # 3. Check for realistic Default Rate (Business Logic Check)
        default_rate = con.execute("""
            SELECT AVG(default_flag) 
            FROM fact_loans 
            WHERE default_flag IS NOT NULL
        """).fetchone()[0]
        
        if default_rate is None:
            logger.error("Data Quality Exception: Default rate could not be calculated.")
            errors_found += 1
        elif not (0.10 <= default_rate <= 0.35):
            logger.warning(f"Business Logic Alert: Global default rate is {default_rate:.2%}, which is outside expected historical bounds (10% - 35%).")
        else:
            logger.info(f"PASS: Global default rate is realistic ({default_rate:.2%}).")
            
        # 4. Referential Integrity Check (fact to dim_risk)
        orphaned_records = con.execute("""
            SELECT COUNT(*) 
            FROM fact_loans f
            LEFT JOIN dim_risk d ON f.risk_key = d.risk_key
            WHERE d.risk_key IS NULL
        """).fetchone()[0]
        
        if orphaned_records > 0:
            logger.error(f"Data Quality Exception: Found {orphaned_records} orphaned records in fact_loans with no matching risk_key in dim_risk.")
            errors_found += 1
        else:
            logger.info("PASS: Referential integrity maintained between fact_loans and dim_risk.")

        # Summary
        if errors_found == 0:
            logger.info("SUCCESS: All Data Quality checks passed. Data is safe for Power BI consumption.")
        else:
            logger.error(f"FAILURE: {errors_found} critical data quality errors detected. Power BI refresh should be halted.")

    except Exception as e:
        logger.error(f"Unexpected error during data quality checks: {e}")
    finally:
        con.close()
        logger.info("Database connection closed.")

if __name__ == "__main__":
    main()
