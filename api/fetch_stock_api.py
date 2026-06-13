import requests
import sys

from helpers.user_input import get_stock, get_quantity
from helpers.terminal_output import to_usd


def get_all_stocks_info(base_url, apikey):
    print()
    stocks = {}
    while True:
        try:
            stock = get_stock()
        except EOFError:
            print("\n")
            return stocks

        if (stock not in stocks) and not stock_symbol_lookup(base_url, apikey, stock):
            print(f"{stock} not found in US exchanges NYSE, Nasdaq\n")
            continue

        try:
            price = fetch_stock_price(base_url, apikey, stock)
        except Exception as e:
            sys.exit(f"Unknown Exception:\n{type(e)}\n{e}")

        print(f"Price of {stock} is {to_usd(price)}")

        quantity = get_quantity(stock)

        if stock not in stocks:
            stocks[stock] = {"last_price": price, "quantity": quantity, "investment": price * quantity}
        else:
            stocks[stock]["last_price"] = price
            stocks[stock]["quantity"] += quantity
            stocks[stock]["investment"] += price * quantity

        print("\n")


def stock_symbol_lookup(base_url, apikey, stock):
    print(f"\nSymbol lookup for {stock} initiated!")
    url = f"{base_url}/search"
    params = {
        "q": stock,
        "exchange": "US",
        "token": apikey
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.HTTPError as he:
        sys.exit(f"HTTPError during symbol lookup\n{he}")
    except requests.ConnectionError as ce:
        sys.exit(f"ConnectionError\n{ce}")
    except requests.RequestException as rqe:
        sys.exit(f"RequestException\n{rqe}")
    except KeyboardInterrupt:
        sys.exit("Exiting!")
    except Exception as e:
        sys.exit(f"Unknown exception\n{e}")

    try:
        data = response.json()
    except requests.JSONDecodeError as je:
        sys.exit(f"Error parsing data! JSONDecodeError\n{je}")
    except KeyboardInterrupt:
        sys.exit("Exiting!")
    except Exception as e:
        sys.exit(f"Unknown exception\n{e}")

    print(f"Lookup results: {data['count']}")
    print(f"Scanning {data['count']} results")

    for result in data["result"]:
        if result["symbol"] == stock:
            print(f"Symbol lookup for {stock} successful!")
            return True
    return False


def fetch_stock_price(base_url, apikey, stock):
    print(f"\nFetching price of {stock}!")
    params = {
        "symbol": stock,
        "token": apikey
    }
    url = f"{base_url}/quote"

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.HTTPError as he:
        sys.exit(f"HTTPError:\n{type(he)}\n{he}")
    except requests.ConnectionError as ce:
        sys.exit(f"ConnectionError check you internet connectivity:\n{type(ce)}\n{ce}")
    except requests.Timeout as te:
        sys.exit(f"Timeout:\n{type(te)}\n{te}")
    except requests.RequestException as rqe:
        sys.exit(f"RequestException:\n{type(rqe)}\n{rqe}")
    except KeyboardInterrupt:
        sys.exit("Exiting!")
    except Exception as e:
        sys.exit(f"Unknown exception:\n{type(e)}\n{e}")

    try:
        data = response.json()
    except requests.JSONDecodeError as je:
        sys.exit(f"Error Parsing queried data!\n\nJSONDecodeError:\n\n{type(je)}\n\n{je}")
    except KeyboardInterrupt:
        sys.exit("Exiting!")
    except Exception as e:
        sys.exit(f"Unknown exception:\n{type(e)}\n{e}")

    price = data["c"]
    try:
        price = float(price)
    except ValueError:
        sys.exit("Error parsing queried price as float")

    print(f"Price fetching of {stock} successful!\n")
    return price

