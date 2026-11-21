import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")
API_KEY = os.getenv("ALPHAVINTAGE_API_KEY")

ROOT = Path(__file__).resolve().parents[1]