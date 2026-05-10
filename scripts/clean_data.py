import pandas as pd
import os

tickers = ["XLK", "XLF", "XLE", "XLV", "XLC", "XLY", "XLP", "XLI", "XLB", "XLU", "XLRE"]

os.makedirs("data/cleaned", exist_ok=True)


def load_raw(ticker):
    path = f"data/raw/{ticker}.csv"
    df = pd.read_csv(path, header=[0, 1], index_col=0, parse_dates=True)
    print(f"Loaded {ticker} from {path}")
    return df


def clean(df, ticker):
    print(f"Cleaning {ticker}...")

    # Keep only Close price
    df = df[["Close"]].copy()
    df.columns = ["price"]

    # Clean index
    df.index = pd.to_datetime(df.index)
    df.index.name = "date"

    # Drop nulls and duplicates
    df.dropna(inplace=True)
    df = df[~df.index.duplicated(keep="first")]
    df.sort_index(inplace=True)

    # Add ticker
    df["ticker"] = ticker

    # Daily return (pct change, first row = 0)
    df["daily_return"] = df["price"].pct_change().fillna(0)

    # Indexed price (rebased to 100 at start)
    df["indexed_price"] = df["price"] / df["price"].iloc[0] * 100

    # Annualized volatility (rolling 252-day, forward filled)
    df["annualized_volatility"] = (
        df["daily_return"]
        .rolling(window=252, min_periods=60)
        .std() * (252 ** 0.5)
    )

    print(f"  {len(df)} rows | vol={df['daily_return'].std() * (252**0.5):.3f} | last price={df['price'].iloc[-1]:.2f}")
    return df


if __name__ == "__main__":
    all_clean = []

    for ticker in tickers:
        df_raw = load_raw(ticker)
        df_clean = clean(df_raw, ticker)
        all_clean.append(df_clean)

    # Combine all tickers
    combined = pd.concat(all_clean)
    combined = combined.reset_index()
    combined = combined[["date", "price", "ticker", "daily_return", "indexed_price", "annualized_volatility"]]

    # Save
    out_path = "data/cleaned/all_sectors_combined.csv"
    combined.to_csv(out_path, index=False)

    print(f"\nSaved to {out_path}")
    print(f"Shape: {combined.shape}")
    print("\nRow counts per ticker:")
    print(combined["ticker"].value_counts().sort_index())
    print(f"\nColumns: {list(combined.columns)}")
    print("\nSample:")
    print(combined.head())
    print("\nCleaning complete.")