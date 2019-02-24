# Robo_Advisor.py

# TODO: import some modules and/or packages here
# TODO: write some Python code here to produce the desired functionality...

#formulate inputs

import requests
import json

# using JSON not CSV
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
response = requests.get(request_url)
# print(type(response))
# print(response.status_code)
# print(response.text)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

# breakpoint()


#outputs below

print("-----------------------")
print("STOCK SYMBOL: AMZN")
print("-----------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: __________")
print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"LATEST DAY: {last_refreshed}")
print("LATEST CLOSING PRICE: $1,259.19")
print("RECENT HIGH: ______")
print("RECENT LOW: ______")

# ... etc.

