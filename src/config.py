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
CSV = ROOT / "data" / "processed" / "covid19_vs_stock.csv"
LINE_FIG = ROOT / "docs" / "line_fig.png"
LINE_FIG2 = ROOT / "docs" / "line_fig2.png"
HIST_FIG = ROOT / "docs" / "hist_fig.png"
SCATTER_FIG = ROOT / "docs" / "scatter_fig.png"