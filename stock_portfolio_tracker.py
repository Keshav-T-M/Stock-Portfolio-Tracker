import yfinance as yf
import pandas as pd
import os

#THIS FUNCTION WILL CLEAR THE TERMINAL SCREEN
def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

#THIS FUNTIOON WILL CHECK IF THE STOCK TICKER IS VALID OR NOT
def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.info 
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None
