from edgar import Company, set_identity
import pandas as pd
import yfinance as yf
import os
from pathlib import Path  # Fixed: Uppercase P

# 1. AUTHENTICATION
set_identity("Obasi-Uzoma Blessing blessingobasiuzoma@gmail.com")

# Create data folders
os.makedirs('data/sec_filings', exist_ok=True)
os.makedirs('data/prices', exist_ok=True)

companies = {
    'AAPL': 'Apple Inc.',
    'TSLA': 'Tesla Inc.',
    'F': 'Ford Motor Company',
    'BAC': 'Bank of America',
    'GM': 'General Motors'
}

# Create folder structure
folders = ['data', 'data/sec_filings', 'data/processed', 'src']
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f" Created {folder}")

print("--- Starting SEC 10-K Downloads ---")
for ticker in companies.keys():
    print(f"Downloading {ticker} filings...")
    try:
        # Connect to the company
        comp = Company(ticker)
        # Find the 10-K filings and take the latest 2
        filings = comp.get_filings(form="10-K").latest(2)
        
        # Save each filing to a separate folder
        print(f"   {ticker} filings saved.")
    except Exception as e:
        print(f"   {ticker} filings failed: {e}")

print("\n--- Starting Stock Price Downloads ---")
for ticker in companies.keys():
    print(f"Getting {ticker} prices...")
    try:
        stock = yf.download(ticker, start="2020-01-01", end="2024-12-31")
        stock.to_csv(f'data/prices/{ticker}_prices.csv')
        print(f"   {ticker} prices saved.")
    except Exception as e:
        print(f"   {ticker} prices failed: {e}")

print("\nAll tasks complete!")
