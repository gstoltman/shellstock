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

    one_year_ago = datetime.now() - timedelta(days=365)
    df = df[df.index > one_year_ago]

    print(df['Price'])

    price_list = df['Price'].tolist()

    print(price_list)

    return price_list

def plot_performance(price_list, symbol):
    max_width = 60
    max_value = max(price_list)
    min_value = min(price_list)
    normalized_data = [(value - min_value) / (max_value - min_value) * max_width for value in price_list]

    height = 20
    canvas = [[' ' for _ in range(max_width + 1)] for _ in range(height)]

    for i, value in enumerate(normalized_data):
        x = int(value)
        y = i * (height // len(price_list))  # Distribute points along the Y-axis
        canvas[y][x] = '*'  # Mark the point

    for row in canvas:  # Reverse to have the low values at the bottom
        print(''.join(row))

def main():
    symbol = input('Enter stock symbol: ').upper()
    price_list = fetch_stock_data(symbol)
    plot_performance(price_list, symbol)

if __name__ == '__main__':
    main()

