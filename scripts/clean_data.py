import pandas as pd
import os

tickers = ["XLK","XLF","XLE","XLV","XLC","XLY","XLP","XLI","XLB","XLU","XLRE"]

os.makedirs("data/cleaned", exist_ok=True)

def load_raw(ticker):
    path = f"data/raw/{ticker}.csv"
    df = pd.read_csv(path, header=[0,1], index_col=0, parse_dates=True)
    print(f"\n{'='*40}")
    print(f"Loaded {ticker} from {path}")
    return df

def inspect(df, ticker):
    print(f"\n--- {ticker} Inspection ---")
    print(f"  Shape:      {df.shape[0]} rows x {df.shape[1]} cols")
    print(f"  Date range: {df.index.min().date()} to {df.index.max().date()}")
    print(f"  Nulls:\n{df.isnull().sum()}")
    print(f"  Adj Close stats:\n{df['Adj Close'].describe().round(2)}")

def clean(df, ticker):
    print(f"\n--- Cleaning {ticker} ---")

    # Keep only Adj Close, rename to price
    df = df[["Adj Close"]].copy()
    df.columns = ["price"]

    # Ensure datetime index
    df.index = pd.to_datetime(df.index)
    df.index.name = "date"

    # Drop nulls
    before = len(df)
    df.dropna(inplace=True)
    dropped = before - len(df)
    print(f"  Nulls dropped:     {dropped}")

    # Remove duplicate dates
    dupes = df.index.duplicated().sum()
    if dupes > 0:
        df = df[~df.index.duplicated(keep="first")]
    print(f"  Duplicate dates:   {dupes}")

    # Sort ascending
    df.sort_index(inplace=True)

    # Flag big single-day moves (>20%)
    df["daily_return"] = df["price"].pct_change()
    big_moves = df[df["daily_return"].abs() > 0.20]
    if not big_moves.empty:
        print(f"  Warning — {len(big_moves)} day(s) with >20% move:")
        print(big_moves)
    else:
        print(f"  No suspicious price moves found")

    # Drop helper column
    df.drop(columns=["daily_return"], inplace=True)

    # Add ticker label
    df["ticker"] = ticker

    print(f"  Final shape:       {df.shape[0]} rows")
    return df

def save(df, ticker):
    path = f"data/cleaned/{ticker}_clean.csv"
    df.to_csv(path)
    print(f"  Saved -> {path}")

if __name__ == "__main__":
    all_clean = []

    for ticker in tickers:
        df_raw   = load_raw(ticker)
        inspect(df_raw, ticker)
        df_clean = clean(df_raw, ticker)
        save(df_clean, ticker)
        all_clean.append(df_clean)

    # Build master combined file
    print(f"\n{'='*40}")
    print("Building master file...")
    master = pd.concat(all_clean)
    master_path = "data/cleaned/all_sectors_combined.csv"
    master.to_csv(master_path)
    print(f"Saved -> {master_path}")
    print(f"Master shape: {master.shape}")
    print("\nRow counts per ticker:")
    print(master["ticker"].value_counts())
    print("\nCleaning complete.")