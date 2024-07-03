import pandas as pd
import yfinance as yf
import json
import os
from datetime import datetime

# List of ticker symbols
tickers = ['AAPL', 'MSFT', 'GOOGL']

# Function to fetch data for a given ticker
def fetch_stock_data(ticker):
    data = yf.download(ticker, start=datetime.today().strftime('%Y-%m-%d'), end=datetime.today().strftime('%Y-%m-%d'))
    data.reset_index(inplace=True)
    return data

# Function to load existing JSON data
def load_json_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return []

# Function to save data to JSON
def save_json_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4, default=str)

# Main function to fetch and append data for all tickers
def update_stock_data(tickers):
    today_str = datetime.today().strftime('%Y-%m-%d')
    
    for ticker in tickers:
        # Fetch new data
        new_data = fetch_stock_data(ticker).to_dict(orient='records')
        
        # Define file path
        file_path = f'{ticker}.json'
        
        # Load existing data
        existing_data = load_json_data(file_path)
        
        # Check for duplicates
        existing_dates = {record['Date'] for record in existing_data}
        new_data = [record for record in new_data if record['Date'] not in existing_dates]
        
        if new_data:
            # Append new data
            updated_data = existing_data + new_data
            
            # Save updated data back to JSON
            save_json_data(file_path, updated_data)
        else:
            print(f"No new data to append for {ticker}")

# Run the update function
update_stock_data(tickers)
