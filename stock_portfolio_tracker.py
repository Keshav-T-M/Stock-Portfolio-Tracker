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

#THIS FUNCTIO WILL CALCULATE THE TOTAL HOLDING PORTFOLIO VALUE AND RETURN IT
def calculate_portfolio_value(portfolio):
    """Calculates the total value of the portfolio."""
    total_value = 0
    for ticker, data in portfolio.items():
        quantity = data.get('quantity', 0) 
        current_price = data.get('currentPrice', 0)  
        total_value += quantity * current_price
    return total_value
