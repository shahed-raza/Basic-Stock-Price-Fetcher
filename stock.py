from dotenv import load_dotenv
import os

from api.fetch_stock_api import get_all_stocks_info
from helpers.user_input import does_user_wants_to_save
from helpers.save_to_csv import save_results
from helpers.terminal_output import print_table, to_usd


load_dotenv(".env")

apikey = os.getenv("STOCK_API_KEY")
base_url = "https://finnhub.io/api/v1"


def main():
    print("Enter Ctrl+C to exit and Ctrl+D to stop asking for stock symbol")

    stocks_info = get_all_stocks_info(base_url, apikey)

    total_investment = sum(stocks_info[stock]["price"] * stocks_info[stock]["quantity"] for stock in stocks_info.keys())

    if (does_user_wants_to_save()):
        save_results(stocks_info)

    print_table(stocks_info)

    print(f"\nTotal Investment: {to_usd(total_investment)}")


if __name__ == "__main__":
    main()
