import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import api_key

def fetch_stock_data(symbol):
    API_KEY = api_key.api_key
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&outputsize=compact&apikey={API_KEY}'

    r = requests.get(url)
    data = r.json()

    df = pd.DataFrame(data['Monthly Time Series']).T
    df = df.rename(columns={'4. close': 'Price'})
    df['Price'] = df['Price'].astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index(ascending=True)

    one_year_ago = datetime.now() - timedelta(days=365)
    df = df[df.index > one_year_ago]
    
    return df

def main():
    symbol = input('Enter stock symbol: ').upper()
    stock_df = fetch_stock_data(symbol)
    print(f'\n===== Past Year of Closing Prices for {symbol} =====\n\n')
    print(stock_df['Price'])

if __name__ == '__main__':
    main()

