

from sec_edgar_downloader import Downloader
import pandas as pd
import yfinance as yf
import os

# Create data folder
os.makedirs('data', exist_ok=True)

# Download SEC filings for 5 companies (start small!)
companies = {
    'AAPL': 'Apple Inc.',
    'TSLA': 'Tesla Inc.',
    'F': 'Ford Motor Company',
    'BAC': 'Bank of America',
    'GM': 'General Motors'
}

print("Downloading SEC 10-K filings...")
dl = Downloader("Obasi-Uzoma Blessing", "blessingobasiuzoma@gmail.com", "data/sec_filings")

for ticker in companies.keys():
    print(f"Downloading {ticker}...")
    try:
        # Download last 2 years of 10-K filings
        dl.get("10-K", ticker, limit=2)
        print(f" {ticker} done")
    except Exception as e:
        print(f" {ticker} failed: {e}")

print("\nDownloading stock price data...")
for ticker in companies.keys():
    print(f"Getting {ticker} prices...")
    try:
        stock = yf.download(ticker, start="2020-01-01", end="2024-12-31")
        stock.to_csv(f'data/{ticker}_prices.csv')
        print(f" {ticker} saved")
    except Exception as e:
        print(f" {ticker} failed: {e}")

print("\n Data collection is complete.")
