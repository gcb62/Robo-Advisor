# Robo_Advisor.py

# TODO: import some modules and/or packages here
# TODO: write some Python code here to produce the desired functionality...

#formulate inputs

import csv
import json
import os
from dotenv import load_dotenv
load_dotenv()

import requests

import datetime as datetime

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


# using JSON not CSV
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
print(api_key)

symbol = "MSFT"
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey={symbol}"
response = requests.get(request_url)


parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

# breakpoint()

time_series = parsed_response["Time Series (Daily)"]

dates = list(time_series.keys()) # assume days are in descending order

latest_day = dates[0]

latest_close = time_series[latest_day]["4. close"]

high_prices = []
low_prices = []

for date in dates:
    high_price = time_series[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = time_series[date]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

now = datetime.datetime.now()

#outputs below

# csv_file_path = "data/prices.csv" # a relative filepath

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        dayprice = time_series[date]
        writer.writerow({
            "timestamp": date,
            "open": dayprice["1. open"],
            "high": dayprice["2. high"],
            "low": dayprice["3. low"],
            "close": dayprice["4. close"],
            "volume": dayprice["5. volume"]
        })




print("-----------------------")
print("STOCK SYMBOL: AMZN")
print("-----------------------")



print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: " + now.strftime("%Y-%m-%d %H:%M:%S"))
print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSING PRICE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-----------------------")
print("YOU SHOULD: ___")
print("Because: ___")
print("-----------------------")
print(f"Writing Data to CSV: {csv_file_path}...")
print("-----------------------")
print("Good luck!")


