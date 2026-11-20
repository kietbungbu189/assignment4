from pathlib import Path

ROOT = Path(__File__).Resolve().parent.parent
CSV_D = ROOT / "data" / "raw" / "deaths_global.csv"
CSV_C = ROOT / "data" / "raw" / "cases_global.csv"
FILE_OR_ADDRESS = 