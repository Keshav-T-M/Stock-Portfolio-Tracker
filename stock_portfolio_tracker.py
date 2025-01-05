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

#THIS FUNCTION WILL CALCULATE THE TOTAL HOLDING PORTFOLIO VALUE AND RETURN IT
def calculate_portfolio_value(portfolio):
    """Calculates the total value of the portfolio."""
    total_value = 0
    for ticker, data in portfolio.items():
        quantity = data.get('quantity', 0) 
        current_price = data.get('currentPrice', 0)  
        total_value += quantity * current_price
    return total_value

#THIS FUNCTION WILL DISPLAY THE SUMMARY OF THE PORTFOLIO (TOTAL VALUE AND NUMBER OF HOLDINGS)
def display_portfolio_summary(portfolio):
    """Displays a concise summary of the portfolio."""
    clear_screen()
    total_value = calculate_portfolio_value(portfolio)
    if not portfolio:
        print("Your portfolio is empty.")
        return

    print("\n--- Portfolio Summary ---")
    print(f"Total Value: ${total_value:.2f}")
    print(f"Number of Holdings: {len(portfolio)}")
    print("-" * 20)

#THIS FUNCTION WILL DISPLAY THE DETAILED PORTFOLIO
def display_detailed_portfolio(portfolio):
    """Displays the current stock portfolio with detailed information."""
    display_portfolio_summary(portfolio)  


def main():
    portfolio = {}
#ASKING USER TO SELECT THE OPTION
    while True:
        clear_screen()  
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Detailed Portfolio")
        print("4. Export Portfolio (CSV)") 
        print("5. Exit")

        choice = input("Enter your choice: ")
# HERE THE IF WILL CHECK THE INSERTED OPTION (CHOICE)
        if choice == '1':
            ticker = input("Enter stock ticker (e.g., AAPL): ").upper()
            quantity = int(input("Enter quantity: "))
            stock_data = get_stock_data(ticker)

            if stock_data:
                if ticker in portfolio:
                    portfolio[ticker]['quantity'] += quantity
                else:
                    portfolio[ticker] = stock_data
                    portfolio[ticker]['quantity'] = quantity
                print(f"{ticker} added to portfolio.")
            input("Press Enter to continue...")

        elif choice == '2':
            ticker = input("Enter stock ticker to remove: ").upper()
            if ticker in portfolio:
                del portfolio[ticker]
                print(f"{ticker} removed from portfolio.")
            else:
                print(f"{ticker} not found in portfolio.")
            input("Press Enter to continue...")

        elif choice == '3':
            display_detailed_portfolio(portfolio)
            input("Press Enter to continue...")

        elif choice == '4':  # New feature: Export to CSV
            if not portfolio:
                print("Your portfolio is empty. Nothing to export.")
                input("Press Enter to continue...")
                continue

            try:
                df = pd.DataFrame(portfolio).T
                df.to_csv("portfolio.csv", index=False)
                print("Portfolio successfully exported to portfolio.csv")
            except Exception as e:
                print(f"Error exporting portfolio: {e}")
            input("Press Enter to continue...")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()

# Example Stock Tickers 
# AAPL 
# GOOG 
# AMZN 
# TSLA
# MSFT 
# JPM 
# FB 
# BRK.A 
# BAC
# WMT 