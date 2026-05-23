import os
import subprocess
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))
os.environ["KAGGLE_TOKEN"] = os.getenv("KAGGLE_TOKEN")

kaggle_cli = r"C:\Users\alexa\AppData\Local\Python\pythoncore-3.14-64\Scripts\kaggle.exe"

subprocess.run([
    kaggle_cli, "datasets", "download",
    "-d", "wordsforthewise/lending-club",
    "-p", "data/bronze/",
    "--unzip"
])

print("Download complete!")