from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_D = ROOT / "data" / "raw" / "COVID19" / "deaths_global.csv"
CSV_C = ROOT / "data" / "raw" / "COVID19" / "cases_global.csv"
TARGET_FILEORADDRESS = f"https://alphavantage.co{symbol}&apikey={api_key}"
ALPHA_VANTAGE_API_KEY = "AQBXLQR83N391L55"
LOG = ROOT / "logs" / "log.txt"
TEST_PRINT = ROOT / "notebooks" / "test_print.txt"