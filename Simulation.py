import bybit
import os
import time
import numpy as np
import csv
from tkinter.constants import END, TRUE, Y
import matplotlib
from matplotlib import pyplot as plt
from pybit import HTTP

class transaction:
    def __init__(self,n,price,amount,action):
        self.id = n
        self.price = price
        self.amount = amount
        self.action = action

class wallet:
    def __init__(self,total_btc,total_cash,btc_price,transaction):
        self.total_btc = total_btc
        self.total_cash = total_cash

        if (transaction.action == 'buy'):
            self.total_btc = self.total_btc - transaction.amount
        if (transaction.action == 'sell'):
            self.total_btc = self.total_btc + transaction.amount

        self.total_value = self.total_btc * btc_price + self.total_cash

        # conversion function    
def convertTuple(tup):
	str = ' '.join(tup)
	return str

 
def writeToList(list,price,amount):
    list.write(str(price))
    list.write(" ")
    list.write(str(amount))
    list.write('\n')      

# Open CSV file of BTC price history and convert to txt file
with open("BitcoinHistoricalData.csv","r") as csv_file:
    for row in reversed(list(csv.reader(csv_file))):
        list = open("BitcoinHistoricalData.txt",'a')
        list.write(' ,'.join(row))
        list.write('\n')
	

btc_date = []
btc_price = []
for line in open('BitcoinHistoricalData.txt', 'r'):
    lines = [i for i in line.split()]
    date_lines = lines[0],lines[1],lines[2]
    btc_date.append(convertTuple(date_lines))
    btc_price.append(lines[4].replace(',','')) #remove , from dataset

btc_hist_data =  btc_date,btc_price # x- date, y - btc price

# Case 1: buy everyday and sell only when x10
total_cash = 1000000
n = len(btc_hist_data[0])
buy_per_day = total_cash / n
sell_x = 2

k = 0
m = 2
_list_array = np.zeros((m, n))

list_of_transactions = []
for i in range(0,n-1):
    if float(btc_price[i]) > 0 :

        # buy list creation
        buy_price = float(btc_price[k])
        buy_quantity = buy_per_day / float(buy_price)
        buy_list = open("Buy_List.txt",'a')
        writeToList(buy_list,buy_price,buy_quantity)
        _list_array[0][k] = buy_price
        _list_array[1][k] = buy_quantity

        for j in range(0,k):

            bought_price = _list_array[0][j]
            current_price = float(btc_price[k])
            sell_condition =  current_price >= bought_price*sell_x and bought_price > 0

            if (sell_condition):
                sell_price = btc_price[k]
                sell_quantity = _list_array[1][j]
                #print(sell_quantity)
                
                sell_list = open('Sell_List.txt','a')
                writeToList(sell_list,sell_price,sell_quantity)
                _list_array[0][j] = 0
                _list_array[1][j] = 0
                    
    k = k + 1
