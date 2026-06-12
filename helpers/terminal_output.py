import tabulate


def print_table(stocks_info):
    header = ["Stock Symbol", "Price", "Quantity", "Investment"]
    rows = []
    for stock in stocks_info.keys():
        price = stocks_info[stock]["price"]
        quantity = stocks_info[stock]["quantity"]
        investment = price * quantity 
        row = [stock, to_usd(price), quantity, to_usd(investment)]
        rows.append(row)
    table = tabulate.tabulate(rows, header, "simple_grid")
    print(table)


def to_usd(num):
    return "${:,.2f}".format(num)
