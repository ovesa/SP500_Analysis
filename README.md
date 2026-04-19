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

'''
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
'''

## Key findings

1. Sector leadership rotates with the macro regime. No sector wins in every environment
2. XLE had the widest return range of any sector: -56% in the COVID crash, +148% in the rate hike era
3. XLP and XLV are the most defensive with the lowest crash losses, lowest volatility, lowest bull market upside
4. All sectors are positively correlated. Correlation goes to 1 in a crash regardless of sector
5. XLRE was the only sector negative in the rate hike era (-8.1%) due to its sensitivity to borrowing costs

## Dashboard

[View on Power BI](https://app.powerbi.com/view?r=eyJrIjoiODBkMzcyM2QtYzNiOC00NGFiLWJiN2UtMGJmNGZjMTViYmY1IiwidCI6IjM5NjU3M2NiLWYzNzgtNGI2OC05YmM4LTE1NzU1YzBjNTFmMyIsImMiOjZ9)
