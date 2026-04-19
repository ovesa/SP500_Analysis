# S&P 500 Sector Performance Dashboard

Analysis of historical S&P 500 sector ETF performance (2018–2026) built end to end in Python and Power BI.

## Project covers

- Sector returns, volatility, and correlation across four distinct market cycles
- Python pipeline for data collection, cleaning, and EDA
- Interactive Power BI dashboard with cycle and sector filtering

## Dashboard pages

### 1. Performance

Normalized price performance rebased to 100 at the start date. Filterable by sector. Shows the full divergence between XLK, XLE, and the defensive sectors over the period.

### 2. Volatility

Annualized volatility ranking by sector. XLE is the most volatile, XLP and XLRE the least. Confirms the defensive vs cyclical character of each sector.

### 3. Correlation

Pearson correlation heatmap of daily returns. All sectors are positively correlated. XLE vs XLK is the lowest pair at 0.54. Sector diversification does not protect against systemic shocks.

### 4. Market Cycles

Interactive cycle selector across four macro regimes. Rebases performance to 100 at the start of each cycle to isolate
sector behavior within that environment.

## Tools

- Python 3.12 — yfinance, pandas, matplotlib, seaborn
- Power BI (app.powerbi.com)

## Project structure

```text
SP500_Analysis/
├── data/
│   ├── raw/              # Raw CSVs from yfinance
│   └── cleaned/          # Cleaned and combined data
├── notebooks/
│   └── eda.ipynb      # Full exploratory analysis
├── scripts/
│   ├── download_data.py  # Downloads raw ETF data
│   ├── clean_data.py     # Cleans and validates data
│   └── run_pipeline.py   # Runs full pipeline end to end
├── .gitignore
├── requirements.txt
└── README.md
```

## Key findings

## Key findings

1. **Sector leadership rotates with the macro regime.** No sector wins in every environment. XLK led pre-COVID (+46.9%) and the recover (+127.4%). XLE dominated the rate hike era (+148.7%). XLP held up best in the crash, losing only 24.2% when every other sector lost more. Leadership is regime-dependent, not structural, which is the core argument for building a cycle-aware dashboard rather than static ranking.

2. **XLE is in a category of its own for volatility and return range.** Annualized volatility of 32.1%, roughly 10 percentage points above the cross-sector average of 22.5%. The return spread across cycles runs from -56% in the COVID crash to +148.7% in the rate hike era. No other sector comes close to that range. Energy is not just volatile in the statistical sense, it is driven by a completely different set of factors (commodity prices, geopolitics, supply shocks) than the rest of the index.

3. **XLP and XLV are the only genuinely defensive sectors in the dataset.** XLP has the lowest annualized volatility at 15.6% and the tightest daily return distribution with a sigma of 0.010. XLV sits at 17.5%. Both sectors rank near the bottom in bull market returns and near the top in crash resilience every single cycle. That consistency is the point. Defensive sectors are not underperformers, they are a different instrument entirely.

4. **All sectors are positively correlated. There is no hedge within the S&P 500 sector universe.** The lowest pair in the full period correlation matrix is XLE vs XLU at 0.38, followed by XLE vs XLK at 0.43. Every other pair sits above 0.5. The rolling volatility chart makes the practical implication clear: in March 2020 every sector spiked simultaneously regardless of how different their normal behavior is. Sector diversification reduces day-to-day volatility but does not protect you when the whole market moves.

5. **XLRE was the only sector to finish negative in the rate hike era at -8.1%.** Real estate investment trusts borrow heavily to buy property. When the Fed hiked rates from near zero to above 5% in roughly 18 months, the cost of that debt roughly doubled and REIT valuations compressed directly. XLU is also rate-sensitive but managed +47.3% over the same period because regulated utility revenues provided a partial offset. The difference between those two outcomes is worth understanding before building any rate-sensitive position.

## Dashboard

[View on Power BI](https://app.powerbi.com/view?r=eyJrIjoiODBkMzcyM2QtYzNiOC00NGFiLWJiN2UtMGJmNGZjMTViYmY1IiwidCI6IjM5NjU3M2NiLWYzNzgtNGI2OC05YmM4LTE1NzU1YzBjNTFmMyIsImMiOjZ9)
