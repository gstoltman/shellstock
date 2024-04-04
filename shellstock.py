import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import api_key

def fetch_stock_data(symbol):
    API_KEY = api_key.api_key
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={API_KEY}'

    r = requests.get(url)
    data = r.json()

    df = pd.DataFrame(data['Time Series (Daily)']).T
    df = df.rename(columns={'1. open': 'Open', '4. close': 'Close'})
    df[['Open', 'Close']] = df[['Open', 'Close']].astype(float)
    df.index = pd.to_datetime(df.index)

    one_year_ago = datetime.now() - timedelta(days=365)
    df = df[df.index > one_year_ago]

    return df

def plot_performance(df, symbol):
    plt.figure(figsize=(10, 5))
    plt.plot(df['Close'], label='Closing Price')
    plt.title('Perf')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def main():
    symbol = input('Enter stock symbol: ').upper()
    df = fetch_stock_data(symbol)
    plot_performance(df, symbol)

if __name__ == '__main__':
    main()

