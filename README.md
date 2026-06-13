# Basic Stock Price Fetcher

## Why does this exist?

* To practice api consumption, basic api querying
* To practice requests module
* To practice writing clean, maintainable code

## What did I actually do?

* Continously take stock symbol inputs from user until they
hit Ctrl+D, Ctrl+C exits program
* For each stock symbol input, a stock symbol lookup is performed
to check it's existence
* If exists, fetches the unit price of the stock symbol
* And then proceeds to ask user for quantity of the stock to buy
* Calculates the total investment based on price and quantity of each stock
* Asks user if they want to save the results as a csv file
* prints the results in table on the command line interface

## What could I have done better?

* Could've thought about how data would flow between functions earlier
in the phase
* I could have improved the modularity of the code
* Could've made it more aesthetically appealing, by adding colors like
green for success, red for errors

## What's missing?

* Interactivity is missing, it lacks TUI
