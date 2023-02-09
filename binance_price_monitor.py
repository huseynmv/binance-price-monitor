import os
import time
from binance.client import Client
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get the API key and secret key from the environment variables
api_key = os.getenv("BINANCE_API_KEY")
secret_key = os.getenv("BINANCE_SECRET_KEY")

# Initialize the Binance client
client = Client(api_key, secret_key)

# Define the symbol for XRP/USDT futures
symbol = "XRPUSDT"

# Continuously read the current price
while True:
    # Get the latest price of XRP/USDT futures
    ticker = client.get_ticker(symbol=symbol)
    current_price = float(ticker["lastPrice"])

    # Get the maximum price for the last hour
    try:
        max_price
    except NameError:
        max_price = current_price

    if current_price / max_price < 0.99:
        print(f"The price of {symbol} futures has fallen by 1% from the maximum price for the last hour.")
        max_price = current_price


    time.sleep(1)

