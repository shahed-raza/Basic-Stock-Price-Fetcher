import csv
import sys
import tabulate


def main():
    # stock_symbol, unit_price, quantity of each stocks in one dict in-case of real-api usage
    stocks_quantity = get_stocks_and_quantities()
    # wouldn't need in-case of real-api usage
    prices = fetch_prices_of_all_stocks(stocks_quantity.keys())
    # way of accessing of unit price, quantity changes in-case of real-api usage
    total_investement = sum(stocks_quantity[stock] * prices[stock] for stock in stocks_quantity)
    if (is_save_to_file()):
        filename = get_csv_filename()
        # all stock info passed as single dict
        save_results(stocks_quantity, prices, filename)
    # all stock info passed as single dict
    pretty_print(stocks_quantity, prices)
    print(f"\nTotal Investment: {total_investement}")


def fetch_stock_price(stock):
    # temporary hardcoded dict, upgrade to api later
    prices = {
        "MMM": 150,
        "AAPL": 180,
        "TSLA": 250,
        "ACN": 160,
        "AMD": 200,
        "GOOG": 198,
        "GOOGL": 174,
        "AMZN": 159
    }
    if stock in prices:
        return prices[stock]
    else:
        raise KeyError


# not needed in-case of real-api usage
def fetch_prices_of_all_stocks(stocks):
    prices = {}
    for stock in stocks:
        price = fetch_stock_price(stock)
        prices[stock] = price
    return prices


def is_save_to_file():
    try:
        user_response = input("Do you want to save stock symbol, quantity, and corresponding price in a csv file? (y/n): ")
        if len(user_response) >= 1 and user_response[0].lower() == 'y':
            return True
    except EOFError:
        print()
        pass
    except KeyboardInterrupt:
        sys.exit("Exiting!")
    return False


def get_csv_filename():
    while True:
        try:
            filename = input("Enter filename: ")
            if not is_csv_file(filename):
                print(f"Try Again! {filename} is not a csv file")
            if filename != "" and is_csv_file(filename):
                return filename
        except EOFError:
            print()
            pass
        except KeyboardInterrupt:
            sys.exit("Exiting!")


def is_csv_file(filename):
    split_filename = filename.split(".")
    if len(split_filename) == 2 and len(split_filename[0]) > 0 and split_filename[1].lower() == "csv":
        return True
    return False


# symbol, unit price, quantity of all stocks passed as a single dict in-case of real-api usage
def save_results(stocks_quantity, prices, filename):
    with open(filename, "w") as file:
        fieldnames = ["stock_symbol", "unit_price", "quantity", "investment"]
        dict_writer = csv.DictWriter(file, fieldnames)
        dict_writer.writeheader()
        for stock in stocks_quantity.keys():
            row = {fieldnames[0]: stock, fieldnames[1]: prices[stock], fieldnames[2]: stocks_quantity[stock], fieldnames[3]: prices[stock] * stocks_quantity[stock]}
            dict_writer.writerow(row)

    print()
    print(f"Saved! results to {filename}\n")


# symbol, unit price, quantity of all stocks passed as a single dict in-case of real-api usage
def pretty_print(stocks_quantity, prices):
    header = ["Stock Symbol", "Unit Price", "Quantity", "Investment"]
    rows = []
    for stock in stocks_quantity.keys():
        row = [stock, prices[stock], stocks_quantity[stock], prices[stock] * stocks_quantity[stock]]
        rows.append(row)
    table = tabulate.tabulate(rows, header, "simple_grid")
    print(table)


# returns the single dict with symbols, unit price, quantity of all the user-inputted stocks in-case of real-api usage
def get_stocks_and_quantities():
    print()
    stocks = {}
    while True:
        try:
            stock = get_stock()
        except EOFError:
            print("\n")
            break
        quantity = get_quantity(stock)
        stocks[stock] = quantity
        print()

    return stocks


# returns the stock symbol, unit price as a dict fetched from the real-api
def get_stock():
    while True:
        try:
            stock = input("Enter stock symbol: ")
        except EOFError:
            raise EOFError
        except KeyboardInterrupt:
            sys.exit("Exiting!")

        if stock != "":
            stock = stock.upper()
            # TODO:
            # fetch the stock
            # do the error check
            # check if it exists
            # store the unit_price
            # returnt the dict ==> {symbol: stock, unit_price: price}

            # temporary fix
            try:
                fetch_stock_price(stock)
                return stock # doesn't raise keyerror exception ==> stock exists
            except KeyError:
                print(f"{stock} not found!\n")


def get_quantity(stock):
    while True:
        try:
            quantity = input(f"Enter quantity for {stock}: ")
            try:
                quantity = float(quantity)
                if quantity > 0:
                    return quantity
            except ValueError:
                pass
        except EOFError:
            print()
            pass
        except KeyboardInterrupt:
            sys.exit("Exiting!")


if __name__ == "__main__":
    main()
