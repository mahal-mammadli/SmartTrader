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
   
    # Program to calculate moving average
    window_size = 15

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
 
    i = 0
    above_or_below = []
    above_or_below_percent = []
    while i < len(moving_averages):
        above_or_below.append(moving_averages[i] > btc_price_2021[i])
        above_or_below_percent.append(moving_averages[i]/btc_price_2021[i] * 100 - 100)
        i += 1

    # Simulation of moving average strategy
    total_cash = 1000
    my_wallet = wallet(0,total_cash)
    print ("Initial Wallet Value:")
    print(my_wallet.total_cash)
    print(my_wallet.total_btc)
    n = len(btc_price_2021)

    buy_price = []*n
    buy_quantity =[]*n
    sell_price = []*n
    sell_quantity = []*n

    # total index
    i = 0
    # buy index
    j = 0
    # sell index
    k = 0
    buy_w = 0.7
    sell_w = 1

    bought = 0
    buy_percent_below = -2.35/100
    sell_percent_above = 2.35/100    
    while i < len(moving_averages):

        if bought == 0:
            if ((btc_price_2021[i] - btc_price_2021[i]*buy_percent_below) < moving_averages[i]):
                if (0 != my_wallet.total_cash):
                    buy_price.append(float(btc_price_2021[i]))
                    buy_quantity.append(my_wallet.total_cash*buy_w / float(btc_price_2021[i]))

                    if ( buy_quantity[j] > 0 and my_wallet.total_cash > 100 ):
                        buy_list = open("Buy_List.txt",'a')
                        writeToList(buy_list,buy_price[j],buy_quantity[j])
                        my_wallet.total_btc = my_wallet.total_btc + buy_quantity[j]
                        my_wallet.total_cash = my_wallet.total_cash - buy_quantity[j]*buy_price[j]
                        bought = 1
                    j += 1     
        if bought == 1:
            if ((btc_price_2021[i]*sell_percent_above + btc_price_2021[i]) > moving_averages[i]):
                if (0 != my_wallet.total_btc):
                    sell_price.append(float(btc_price_2021[i]))
                    sell_quantity.append( my_wallet.total_btc*sell_w )
                    if (sell_quantity[k] > 0 ):
                        sell_list = open('Sell_List.txt','a')
                        writeToList(sell_list,sell_price[k],sell_quantity[k])
                        my_wallet.total_btc = my_wallet.total_btc - my_wallet.total_btc*sell_w
                        my_wallet.total_cash = my_wallet.total_cash + sell_quantity[k]*sell_price[k]
                        bought = 0
                    k += 1

        wallet_total_list = open("Wallet_List.txt",'a') 
        last_btc_price = float(btc_price_2021[i])
        wallet_total = my_wallet.total_cash + my_wallet.total_btc * last_btc_price
        writeToList(wallet_total_list,i, wallet_total)
        i += 1

    print(my_wallet.total_cash)
    print(my_wallet.total_btc)  

    return my_wallet, moving_averages, iteration_ma, above_or_below, above_or_below_percent
