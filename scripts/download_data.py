import yfinance as yf
import os
from datetime import date

tickers = ["XLK", "XLF", "XLE", "XLV", "XLC", "XLY", "XLP", "XLI", "XLB", "XLU", "XLRE"]

os.makedirs("data/raw", exist_ok=True)

START_DATE = "2018-01-01"
END_DATE = date.today().isoformat()  # always pulls through today


def download_ticker(ticker):
    print(f"Downloading {ticker} ({START_DATE} to {END_DATE})...")
    try:
        df = yf.download(ticker, start=START_DATE, end=END_DATE)
        if df.empty:
            print(f"  Warning: no data returned for {ticker}")
            return None
        path = f"data/raw/{ticker}.csv"
        df.to_csv(path)
        print(f"  Saved {len(df)} rows to {path}")
        return df
    except Exception as e:
        print(f"  Error downloading {ticker}: {e}")
        return None


if __name__ == "__main__":
    failed = []
    for ticker in tickers:
        result = download_ticker(ticker)
        if result is None:
            failed.append(ticker)

    print("\nAll downloads complete.")
    if failed:
        print(f"Failed tickers: {failed}")
    else:
        print("All tickers downloaded successfully.")