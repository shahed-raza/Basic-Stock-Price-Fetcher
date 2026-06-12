import sys


def get_stock():
    while True:
        try:
            stock = input("Enter stock symbol: ")
        except EOFError:
            raise EOFError
        except KeyboardInterrupt:
            sys.exit("Exiting!")

        if stock != "":
            return stock.upper()


def get_quantity(stock):
    while True:
        try:
            quantity = input(f"Enter quantity for {stock}: ")
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


def does_user_wants_to_save():
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
