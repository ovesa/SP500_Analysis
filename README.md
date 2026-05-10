# S&P 500 Sector Performance Dashboard

Analysis of historical S&P 500 sector ETF performance (2018–present) built end to end in Python and Power BI.

## Project covers

- Sector returns, volatility, and correlation across five distinct market cycles
- Python pipeline for data collection, cleaning, and feature engineering
- Interactive Power BI dashboard with cycle filtering, KPI cards, and correlation heatmap

## Dashboard

[View on Power BI](https://app.powerbi.com/view?r=eyJrIjoiODBkMzcyM2QtYzNiOC00NGFiLWJiN2UtMGJmNGZjMTViYmY1IiwidCI6IjM5NjU3M2NiLWYzNzgtNGI2OC05YmM4LTE1NzU1YzBjNTFmMyIsImMiOjZ9)

## Dashboard pages

### 1. Sector Performance

Four KPI cards showing best total return (XLK, +487%), best YTD 2026 (XLE, +22.8%), highest risk (XLE, 31.6% annualized vol), and lowest volatility (XLP, 15.6%). Normalized price performance rebased to 100 at the start date for all 11 sectors. Shows full divergence between XLK, XLE, and the defensive sectors over the period.

### 2. Risk & Returns

Annualized volatility ranking by sector with risk-based color coding. Total return bar chart sorted by performance. Risk vs return scatter plot with average volatility and return reference lines dividing sectors into four quadrants. XLK sits alone in the high return / above-average risk quadrant. XLP and XLV offer the best risk-adjusted returns. XLE is the most volatile sector.

### 3. Market Cycles

Interactive cycle selector across five macro regimes: Pre-COVID Bull, COVID Crash, Recovery, Rate Hike Era, and AI Bull Run. Dynamic bar chart showing sector returns within the selected cycle with green/red coloring. Dynamic date range card updates with each selection. Key findings summarize which sectors led and lagged in each environment.

### 4. Correlation

Full 11x11 Pearson correlation matrix of daily returns with gradient heatmap coloring. XLK and XLC are the most correlated pair (0.85). They are both tech-driven. XLE and XLK are the least correlated (0.32). They are the best diversification pair. All sectors are positively correlated; sector diversification reduces daily volatility but does not protect against systemic shocks.

## Tools

- Python 3.12 — yfinance, pandas, matplotlib, seaborn
- Power BI (app.powerbi.com)

## Project structure

```text
SP500_Analysis/
├── data/
│   ├── raw/              # Raw CSVs from yfinance
│   └── cleaned/          # Cleaned and combined data
├── figures/              # Python figures of the SP500 analysis
├── notebooks/
│   └── eda.ipynb         # Full exploratory analysis
├── scripts/
│   ├── download_data.py  # Downloads raw ETF data through today
│   ├── clean_data.py     # Cleans, validates, and engineers features
│   └── run_pipeline.py   # Runs full pipeline end to end
├── .gitignore
├── requirements.txt
└── README.md
```
## Data pipeline

The pipeline downloads daily adjusted close prices for all 11 SPDR sector ETFs from Yahoo Finance (2018–present) and outputs a single combined CSV with the following columns:

- `date` — trading date
- `price` — adjusted close price
- `ticker` — sector ETF ticker
- `daily_return` — daily percentage change
- `indexed_price` — price rebased to 100 at the start date
- `annualized_volatility` — rolling 252-day annualized volatility

To update the data: run `python scripts/run_pipeline.py` and upload the output to SharePoint.

## Key findings

1. **Sector leadership rotates with the macro regime.** No sector wins in every environment. XLK led pre-COVID (+61%) and the recovery (+128%). XLE dominated the rate hike era (+58%). XLP held up best in the crash, losing only 21% when every other sector lost more. Leadership is regime-dependent, not structural.

2. **XLE is in a category of its own for volatility and return range.** Annualized volatility of 31.6%, roughly 10 percentage points above the cross-sector average. The return spread across cycles runs from -51% in the COVID crash to +58% in the rate hike era. Energy is driven by a completely different set of factors (commodity prices, geopolitics, supply shocks) than the rest of the index.

3. **XLP and XLV are the only genuinely defensive sectors in the dataset.** XLP has the lowest annualized volatility at 15.6%. XLV sits at 17.5%. Both rank near the bottom in bull market returns and near the top in crash resilience every single cycle. Defensive sectors are not underperformers.

4. **All sectors are positively correlated. There is no hedge within the S&P 500 sector universe.** The lowest pair is XLE vs XLK at 0.32. Every other pair sits above 0.38. In March 2020, every sector spiked simultaneously regardless of normal behavior. Sector diversification reduces day-to-day volatility but does not protect against systemic shocks.
