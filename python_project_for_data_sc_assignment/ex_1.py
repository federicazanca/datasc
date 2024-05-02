"""Stock librayr with python"""
import yfinance as yf
import pandas as pd
import json

#let's get info on apple
#Using the Ticker module we can create an object that will allow us to access functions to extract data
apple = yf.Ticker("AAPL")

#we downloaded from "!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"
#the apple.json file and now we read it

with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
apple_info

#get info on the country keywork for example
apple_info["country"]

#get the share price of the stock over a certain period of time (max, ie since always). returns pandas df
apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()
apple_share_price_data.reset_index(inplace=True)
#just want to see what changes with reset_index
apple_share_price_data.head()
#plot the share price
apple_share_price_data.plot(x="Date", y="Open")
#extract dividends and plot
apple.dividends
apple.dividends.plot()


"""Exercise for me"""
print("start of exercise")
#Now using the Ticker module create an object for AMD (Advanced Micro Devices) with the ticker symbol is AMD called; name the object amd.
amd = yf.Ticker("AMD")
#!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json
with open('amd.json') as json_file:
    amd_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
amd_info

#Question 1 Use the key 'country' to find the country the stock belongs to, remember it as it will be a quiz question.
print("Question 1 Use the key 'country' to find the country the stock belongs to, remember it as it will be a quiz question.")
print(amd_info['country'])
#Question 2 Use the key 'sector' to find the sector the stock belongs to, remember it as it will be a quiz question.
print("Question 2 Use the key 'sector' to find the sector the stock belongs to, remember it as it will be a quiz question.")
print(amd_info['sector'])
#Question 3 Obtain stock data for AMD using the history function, set the period to max. Find the Volume traded on the first day (first row).
print("Question 3 Obtain stock data for AMD using the history function, set the period to max. Find the Volume traded on the first day (first row).")
amd_share_price_data = amd.history(period='max')
print("head")
print(amd_share_price_data.head())
day1 = amd_share_price_data.head(1)
#print(day1)
print("volume")
print(day1.Volume)