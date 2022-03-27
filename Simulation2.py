from pathlib import Path
import bybit
import os
import time
import numpy as np
import csv
from tkinter.constants import END, TRUE, Y
import matplotlib
from matplotlib import pyplot as plt
from pybit import HTTP
from tkinter import *
import pandas as pd

#read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). 
# Don't forget to put the file name at the end of the path + ".csv"
data = pd.read_csv (r'BTC-USD-Data-Minute\Bitstamp_BTCUSD_2021_minute.csv')   
df = pd.DataFrame(data, columns= ['Person Name','Country'])
#print (df)


# Open CSV file of BTC price history and convert to txt file
path = Path("BitcoinHistoricalData_2022_m.txt")
file_exists = path.is_file()
if file_exists == False :    
    with open("BTC-USD-Data-Minute\Bitstamp_BTCUSD_2022_minute.csv","r") as csv_file:
        for row in reversed(list(csv.reader(csv_file))):
            list = open("BitcoinHistoricalData_2022_m.txt",'a')
            list.write(' ,'.join(row))
            list.write('\n')

path = Path("BitcoinHistoricalData_2021_m.txt")
file_exists = path.is_file()
if file_exists == False :    
    with open("BTC-USD-Data-Minute\Bitstamp_BTCUSD_2021_minute.csv","r") as csv_file:
        for row in reversed(list(csv.reader(csv_file))):
            list = open("BitcoinHistoricalData_2021_m.txt",'a')
            list.write(' ,'.join(row))
            list.write('\n')

def Simulation2():
    class transaction:
        def __init__(self,n,price,amount,action):
            self.id = n
            self.price = price
            self.amount = amount
            self.action = action

    class wallet:
        def __init__(self,total_btc,total_cash):
            self.total_btc = total_btc
            self.total_cash = total_cash

            # conversion function    
    def convertTuple(tup):
        str = ' '.join(tup)
        return str

    
    def writeToList(list,price,amount):
        list.write(str(price))
        list.write(" ")
        list.write(str(amount))
        list.write('\n')     

    btc_date = []
    btc_price = []
    for line in open('BitcoinHistoricalData_2022_m.txt', 'r'):
        lines = [i for i in line.split()]
        date_lines = lines[0],lines[1],lines[2]
        btc_date.append(convertTuple(date_lines))
        btc_price.append(lines[7].replace(',','')) #remove , from dataset

    #remove last row in data
    btc_price.pop()
    btc_hist_data =  btc_date,btc_price # x- date, y - btc price
    
    btc_date_2021 = []
    btc_price_2021 = []
    for line in open('BitcoinHistoricalData_2021_m.txt', 'r'):
        lines = [i for i in line.split()]
        date_lines = lines[0],lines[1],lines[2]
        btc_date_2021.append(convertTuple(date_lines))
        btc_price_2021.append(lines[7].replace(',','')) #remove , from dataset

    #remove last row in data
    btc_price_2021.pop()
    btc_hist_data_2021 =  btc_date_2021,btc_price_2021 # x- date, y - btc price    

    total_cash = 1000
    my_wallet = wallet(0,total_cash)
    print ("Initial Wallet Value:")
    print(my_wallet.total_cash)
    print(my_wallet.total_btc)
    n = len(btc_hist_data_2021[0])
    
    # Program to calculate moving average
    window_size = 10

    i = 0
    # Initialize an empty list to store moving averages
    moving_averages = []
    iteration_ma = []
    
    j = 0

    for price in btc_price_2021:
        btc_price_2021[j] = int(float(price))
        j += 1

    # Loop through the array to consider
    # every window of size 3
    while i < len(btc_price_2021) - window_size :
	
	    # Store elements from i to i+window_size
	    # in list to get the current window
            
        window = btc_price_2021[i : i + window_size]
     
     
	    # Calculate the average of current window
        window_average = round(sum(window) / window_size, 2)
	
	    # Store the average of current
	    # window in moving average list
        moving_averages.append(window_average)
        iteration_ma.append(i)
	
	    # Shift window to right by one position
        i += 1
 
    return my_wallet, moving_averages, iteration_ma
