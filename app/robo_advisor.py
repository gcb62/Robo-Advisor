# Robo_Advisor.py

#formulate inputs

import csv
import json
import os
from dotenv import load_dotenv
load_dotenv()

import requests

import datetime as datetime
now = datetime.datetime.now()

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

if __name__ == "__main__":
    

    # using JSON not CSV
    api_key = str(os.environ.get("ALPHAVANTAGE_API_KEY"))
    # print(api_key)

    print("----------------")
    print("THANK YOU FOR CHOOSING BRENNAN INVESTMENTS")
    print("DISCLAIMER: BRENNAN INVESTMENTS IS NOT LIABLE FOR THE LOSS THAT PERTAINS TO ANY OF OUR ADVISORY SERVICES")
    print("----------------")

    while True:
        stock_ticker = input("Enter the ticker of a stock you want to research: ")
        if not stock_ticker.isalpha():
            print("Please make sure to enter name of stock price")
        else:
            data = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + stock_ticker + "&apikey=" + api_key)

            if "Error" in data.text:
                print("The stock you are looking for is not here")
            else:
                break

    # thanks for that Hiep

    symbol = "MSFT"
    # request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey={symbol}"
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + stock_ticker + "&apikey=" + api_key

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
    close_prices = []

    for date in dates:
        high_price = time_series[date]["2. high"]
        high_prices.append(float(high_price))
        low_price = time_series[date]["3. low"]
        low_prices.append(float(low_price))
        close_price = time_series[date]["4. close"]
        close_prices.append(float(close_price))

    recent_high = max(high_prices)
    recent_low = min(low_prices)
    mean_close = sum(close_prices)/len(close_prices)
    # s/o to @chenm1997 for help with the mean close



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
    print("STOCK SYMBOL: " + stock_ticker)
    print("-----------------------")
    print("REQUESTING STOCK MARKET DATA...")
    print("YOU REQUESTED YOUR DATA AT: " + (now.strftime("%I:%M %p") + " ON " + (now.strftime("%Y-%m-%d"))))
    print("-----------------------")
    print("CRUNCHING THE DATA...")

    print("-----------------------")
    print(f"THE LATEST TRADING DAY: {last_refreshed}")
    print(f"RECENT HIGH: {to_usd(float(recent_high))}")
    print(f"RECENT LOW: {to_usd(float(recent_low))}")
    print(f"LATEST CLOSING PRICE: {to_usd(float(latest_close))}")
    print(f"RECENT AVERAGE: {to_usd(float(mean_close))}")
    print("-----------------------")

    if float(mean_close)>float(latest_close): 
        print("BRENNAN RECCOMMENDS YOU: BUY")
        print ("BRENNAN'S CALCULATIONS CONCLUDE THAT YOU SHOULD BUY THIS STOCK BECAUSE ITS CLOSING PRICE IS LOWER THAN THE RECENT AVERAGE")
    else:
        print("BRENNAN RECCOMMENDS YOU: DO NOT BUY")
        print ("BRENNAN'S CALCULATIONS CONCLUDE THAT YOU SHOULD NOT BUY THIS STOCK BECAUSE ITS CLOSING PRICE IS HIGHER THAN THE RECENT AVERAGE. THIS COULD POSE BOTH SHORT-TERM AND LONG-TERM CONSEQUENCES")

    print("-----------------------")
    print("Always remember in the stock market that for every buyer, there is a seller")
    print("-----------------------")
    print("Good luck and happy investing!")


    # print(f"Writing Data to CSV: {csv_file_path}...")
