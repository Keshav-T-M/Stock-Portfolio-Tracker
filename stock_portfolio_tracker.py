import yfinance as yf
import pandas as pd
import os

#THIS FUNCTION WILL CLEAR THE TERMINAL SCREEN
def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
