from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_D = ROOT / "data" / "raw" / "COVID19" / "deaths_global.csv"
CSV_C = ROOT / "data" / "raw" / "COVID19" / "cases_global.csv"
TARGET_FILEORADDRESS = "https://www.alphavantage.co/query"
ALPHA_VANTAGE_API_KEY = "AQBXLQR83N391L55"
LOG_DIR = ROOT / "logs" / "log.txt"
TEST_PRINT = ROOT / "notebooks" / "test_print.txt"
TEST_PRINT2 = ROOT / "notebooks" / "test_print2.csv"
TEST_PRINT3 = ROOT / "notebooks" / "test_print3.csv"
TICKER = "AAPL"