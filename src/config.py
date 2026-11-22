import os
import logging
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")
API_KEY = os.getenv("ALPHAVINTAGE_API_KEY")

ROOT = Path(__file__).resolve().parents[1]
RAWDATA = ROOT/"data"/"raw"

SCHEMA = ["symbol", "date", "open", "high", "low", "close", "volume"]
class SchemaError(Exception):
    """Exception for Schema errors"""

    def __init__(self, missing:list):
        self.missing = ', '.join(missing)
        super().__init__("Missing schema/schemas: ")

    def __str__(self):
        return f"Missing schema/schemas: {self.missing}"

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)-7s %(name)s: %(message)s")
logging.FileHandler(ROOT/"logs"/"pipeline.log", encoding="utf-8")
logging.StreamHandler()