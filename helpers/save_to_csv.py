import csv
import sys

from helpers.terminal_output import to_usd


def save_results(stocks_info):
    filename = get_csv_filename()

    with open(filename, "w") as file:
        fieldnames = ["stock_symbol", "last_price", "quantity", "investment"]
        dict_writer = csv.DictWriter(file, fieldnames)
        dict_writer.writeheader()
        for stock in stocks_info.keys():
            price = stocks_info[stock]["last_price"]
            quantity = stocks_info[stock]["quantity"]
            investment = stocks_info[stock]["investment"]
            row = {fieldnames[0]: stock, fieldnames[1]: to_usd(price), fieldnames[2]: quantity, fieldnames[3]: to_usd(investment)}
            dict_writer.writerow(row)

    print()
    print(f"Saved! results to {filename}\n")


def get_csv_filename():
    while True:
        try:
            filename = input("Enter filename: ")
            if not is_csv_file(filename):
                print(f"Try Again! {filename} is not a csv file")
            if filename != "":
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
