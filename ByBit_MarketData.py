from os import write
from time import sleep, time
from pybit import HTTP
from matplotlib import pyplot as plt
from datetime import date, datetime, timedelta

# Python3 code to convert a tuple
# into a string using str.join() method

session = HTTP("https://api-testnet.bybit.com")

def BTCUSD_MarketData():
	def convertTuple(tup):
		str = ','.join(tup)
		return str

	def writeToFile(filename,timestamp):
		list = open(filename,'a')
		list.write(convertTuple(timestamp))
		list.write('\n')
		return list

	print(session.server_time())  
	print(session.latest_information_for_symbol(
		symbol="BTCUSD"	))

	BTCUSD = session.latest_information_for_symbol(symbol="BTCUSD") #returns dictionary
	DATA = BTCUSD['result']
	last_price = DATA[0]['last_price']
	now = datetime.now()
	date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

	# Save as numbers
	btcusd_timestamp = str(time()), last_price
	time_btcusd_price_list = writeToFile('BTCUSD_f.txt',btcusd_timestamp)

	# Save with date and time
	btcusd_timestamp = date_time, last_price
	datetime_price_list = writeToFile('BTCUSD_dt.txt',btcusd_timestamp)

for x in range(1000):
	BTCUSD_MarketData()





