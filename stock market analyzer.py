import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def calculate_moving_average(data, window):
    return data.rolling(window=window).mean()

def visualize_stock_data(stock_data, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data['Close'], label='Close Price')
    plt.plot(stock_data['MA_20'], label='20-day Moving Average')
    plt.plot(stock_data['MA_50'], label='50-day Moving Average')
    plt.title(f'{ticker} Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def main():
    ticker = 'AAPL'  # Apple Inc.
    start_date = '2020-01-01'
    end_date = '2023-01-01'

    stock_data = fetch_stock_data(ticker, start_date, end_date)

    # Calculate moving averages
    stock_data['MA_20'] = calculate_moving_average(stock_data['Close'], 20)
    stock_data['MA_50'] = calculate_moving_average(stock_data['Close'], 50)

    # Visualize the stock data and moving averages
    visualize_stock_data(stock_data, ticker)


if __name__ == '__main__':
    main()

"""
In this example, we define functions to fetch stock data, calculate moving averages, and visualize the results. The main() function puts it all together:

Fetch stock data for the specified ticker and date range using the fetch_stock_data function.
Calculate the 20-day and 50-day moving averages using the calculate_moving_average function.
Visualize the stock data and moving averages using the visualize_stock_data function.
When you run the script, it will download the historical stock data for Apple Inc. (AAPL), calculate the moving averages, and plot the results.

Keep in mind that this is a simple example, and there's much more you can do with a stock market analyzer. You could add more technical indicators, implement prediction algorithms, or build a web app to display the results.


"""

