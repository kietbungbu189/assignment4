from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_CSV = PROJECT_ROOT / "data" / "raw" / "supply_chain" / "fact_supply-chain-data.csv"
DB = PROJECT_ROOT / "data" / "database.db"
LOG = PROJECT_ROOT / "logs" / "log.txt"
MATERIAL_AUGUST = (
    PROJECT_ROOT / "data" / "raw" / "materials" / "august_2025.xlsx"
)
MATERIAL_OCTOBER = (
    PROJECT_ROOT / "data" / "raw" / "materials" / "october_2026.xlsx"
)
MATERIAL_OFFERS = (
    PROJECT_ROOT / "data" / "raw" / "materials" / "supplier_offers.csv"
)