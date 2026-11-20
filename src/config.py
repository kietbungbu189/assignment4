from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_CSV = PROJECT_ROOT / "data" / "raw" / "fact_supply-chain-data.csv"
DB = PROJECT_ROOT / "data" / "database.db"
LOG = PROJECT_ROOT / "logs" / "log.txt"