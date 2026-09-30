# Exchange Rate Normalizer

A Python script that combines exchange rate data from two differently-structured JSON sources into a single, unified format — a common real-world data engineering challenge when integrating multiple APIs or providers.

## How it works
- **Source 1**: a nested JSON object with a base currency and a dictionary of rates
- **Source 2**: a flat list of records using currency pair strings (e.g., "USD/BRL")
- Both sources are transformed into the same schema: `currency`, `rate`, `base_currency`, `date`
- The two normalized datasets are combined with `pd.concat()`
- Duplicate currency/date combinations are removed with `.drop_duplicates()`

## How to run
```bash
python exchange_rate_normalizer.py
```

## What I learned
- Using `pd.json_normalize()` to flatten a nested JSON structure into a DataFrame
- Using `.T` (transpose) and `.reset_index()` to reshape data from wide to long format
- Splitting a combined string column (`currency_pair`) into separate columns with `.str.split(expand=True)`
- Renaming columns to align two differently-shaped datasets into a common schema before combining
- Using `pd.concat()` to stack normalized DataFrames, then `.drop_duplicates()` to clean up overlaps

## Dependencies
Requires pandas:
```bash
pip install pandas
```
