import os
import sys 
import shutil
import glob
import subprocess
import pyarrow.csv as pv
import pyarrow.parquet as pq
from pyarrow.csv import ConvertOptions
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))

# 0. Idempotency Check (Check if Parquet already exists)
parquet_file = "data/bronze/accepted_2007_to_2018Q4.parquet"
already_converted = os.path.exists(parquet_file)

if already_converted:
    print("Dataset already processed and converted to Parquet. Skipping download and conversion.")
else:
    # --- START OF HEAVY PROCESSING ---
    
    # 1. Strict validation (Prevents obscure NoneType errors)
    kaggle_user = os.getenv("KAGGLE_USERNAME")
    kaggle_key = os.getenv("KAGGLE_KEY")

    if not kaggle_user or not kaggle_key:
        print("Critical Error: Missing Kaggle credentials in .env file")
        sys.exit(1)

    os.environ["KAGGLE_USERNAME"] = kaggle_user
    os.environ["KAGGLE_KEY"] = kaggle_key

    # Find kaggle executable dynamically or fallback to hardcoded local path
    kaggle_cli = shutil.which("kaggle") or r"C:\Users\alexa\AppData\Local\Python\pythoncore-3.14-64\Scripts\kaggle.exe"

    # 2. Resilient Download (Check if CSV exists to avoid redundant downloads)
    csv_files = [f for f in glob.glob("data/bronze/**/accepted*.csv", recursive=True) if os.path.isfile(f)]

    if not csv_files:
        print("Downloading dataset from Kaggle...")
        try:
            subprocess.run([
                kaggle_cli, "datasets", "download",
                "-d", "wordsforthewise/lending-club",
                "-p", "data/bronze/",
                "--unzip"
            ], check=True)
            # Refresh the file list cleanly after downloading
            csv_files = [f for f in glob.glob("data/bronze/**/accepted*.csv", recursive=True) if os.path.isfile(f)]
        except subprocess.CalledProcessError as e:
            print(f"Kaggle Error: {e}")
            sys.exit(1)
    else:
        print("Dataset already downloaded, skipping download step.")

    # 3. Secure Path Assignment
    try:
        csv_file = csv_files[0]
    except IndexError:
        print("Error: CSV file not found even after download attempt.")
        sys.exit(1)

    # 4. Flexible conversion to handle messy data types
    print("Converting to Parquet...")
    try:
        # Lending Club dataset has messy types, adding flexibility to PyArrow
        convert_options = ConvertOptions(strings_can_be_null=True)
        table = pv.read_csv(csv_file, convert_options=convert_options)
        pq.write_table(table, parquet_file)
    except Exception as e:
        print(f"Conversion Error: {e}")
        sys.exit(1)

    # 5. Validation and metadata logging
    metadata = pq.read_metadata(parquet_file)
    print(f"Success: Parquet file created ({metadata.num_rows:,} rows).")
    
    # --- END OF HEAVY PROCESSING ---


# 6. Clean up raw extracted CSV folders (THIS ALWAYS RUNS, EVEN IF ALREADY CONVERTED)
print("Checking for raw CSV folders to clean up...")
folders_to_clean = glob.glob("data/bronze/*csv/")
for raw_folder in folders_to_clean:
    shutil.rmtree(raw_folder)
    print(f"Cleaned up: {raw_folder}")
for gz_file in glob.glob("data/bronze/*.gz"):
    os.remove(gz_file)
    
print("Bronze pipeline check completed successfully!")