import yfinance as yf
import os

tickers = ["XLK", "XLF", "XLE", "XLV", "XLC", "XLY", "XLP", "XLI", "XLB", "XLU", "XLRE"]

os.makedirs("data/raw", exist_ok=True)


def download_ticker(ticker):
    print(f"Downloading {ticker}...")
    df = yf.download(ticker, start="2018-01-01", end="2026-04-01")
    path = f"data/raw/{ticker}.csv"
    df.to_csv(path)
    print(f"Saved to {path}")
    return df


if __name__ == "__main__":
    for ticker in tickers:
        download_ticker(ticker)
    print("\nAll raw data downloaded.")
