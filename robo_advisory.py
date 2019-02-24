# Robo_Advisor.py

# TODO: import some modules and/or packages here
# TODO: write some Python code here to produce the desired functionality...

#formulate inputs

import requests
import json
import datetime as datetime

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


# using JSON not CSV
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
response = requests.get(request_url)


parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

# breakpoint()

time_series = parsed_response["Time Series (Daily)"]

dates = list(time_series.keys()) # assume days are in descending order

latest_day = dates[0]

latest_close = time_series[latest_day]["4. close"]



#outputs below

print("-----------------------")
print("STOCK SYMBOL: AMZN")
print("-----------------------")

now = datetime.datetime.now()

print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: " + now.strftime("%Y-%m-%d %H:%M:%S"))
print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSING PRICE: {to_usd(float(latest_close))}")
print("RECENT HIGH: ______")
print("RECENT LOW: ______")

# ... etc.

