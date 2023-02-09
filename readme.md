### Monitoring the Price of Cryptocurrency Pairs on Binance in Real Time using Python

This guide provides instructions on how to create a Python program that reads the current price of cryptocurrency pairs on the Binance exchange in real time and alerts you if the price has fallen by 1% from the maximum price for the last hour.

##### Prerequisites

- Python 3 installed on your system
- Binance API key and secret key
- binance and python-dotenv libraries installed

##### Step 1: Install the Required Libraries

To install the required libraries, run the following command in your terminal:

```python
pip install binance python-dotenv
```

##### Step 2: Create a .env File to Store the API Key and Secret Key

Create a .env file in the same directory as your Python program and add the following lines:

```python
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```

Replace your_api_key and your_secret_key with your actual API key and secret key, respectively.

##### Step 3: Run the Python Program

Save the Python file and run it using the following command in your terminal:

```python
python binance_price_monitor.py
```

The program will now continuously read the current price of the cryptocurrency pair and print a message to the console if the price has fallen by 1% from the maximum price for the last hour.

##### Conclusion

This guide demonstrated how to create a Python program that monitors the price of cryptocurrency pairs on the Binance exchange in real time and alerts you if the price has fallen by 1% from the maximum price for the last hour. You can modify the program to monitor multiple pairs by adding the symbols to a list and looping through the list in the program.

To modify the program so that it processes all pairs, you would need to change the following parts of the code:

Define a list of all the symbols: Instead of defining a single symbol for XRP/USDT futures, you would define a list of all the symbols for the pairs that you want to monitor. This list can be created by calling the Client.`get_exchange_info()` method, which returns information about all the symbols traded on the Binance exchange.

Loop through the list of symbols: Instead of hardcoding the symbol for XRP/USDT futures, you would loop through the list of symbols and call the `get_price` function for each symbol.

Modify the `get_price` function: The `get_price` function would need to take the symbol as an argument and use it to get the latest price of the specified symbol.

Modify the output message: The output message would need to be updated to include the name of the symbol for which the price has fallen by 1% from the maximum price for the last hour.

By making these changes, the program would be able to process all pairs, not just XRP/USDT.
