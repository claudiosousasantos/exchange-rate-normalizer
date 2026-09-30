import json
import pandas as pd

# Source 1: nested JSON structure
raw_json = '''
{
    "base": "USD",
    "date": "2024-01-15",
    "rates": {"BRL": 4.95, "EUR": 0.91, "GBP": 0.78, "JPY": 148.20}
}
'''
data = json.loads(raw_json)
df = pd.json_normalize(data['rates']).T.reset_index()
df.columns = ['currency', 'rate']
df['base_currency'] = data['base']
df['date'] = data['date']

# Source 2: flat list-of-records structure
raw_json_2 = '''
[
    {"currency_pair": "USD/BRL", "exchange_rate": 4.95, "timestamp": "2024-01-15"},
    {"currency_pair": "USD/EUR", "exchange_rate": 0.91, "timestamp": "2024-01-15"},
    {"currency_pair": "USD/CAD", "exchange_rate": 1.35, "timestamp": "2024-01-15"}
]
'''
data_2 = json.loads(raw_json_2)
df2 = pd.DataFrame(data_2)
df2[['base_currency', 'currency']] = df2['currency_pair'].str.split('/', expand=True)
df2 = df2.rename(columns={'exchange_rate': 'rate', 'timestamp': 'date'})
df2 = df2[['currency', 'rate', 'base_currency', 'date']]

# Combine and clean
combined_df = pd.concat([df, df2], ignore_index=True)
combined_df = combined_df.drop_duplicates(subset=['currency', 'date'])

print(combined_df)