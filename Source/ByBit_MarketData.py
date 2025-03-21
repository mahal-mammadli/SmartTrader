from os import write
from time import sleep, time
from pybit.unified_trading import HTTP
from matplotlib import pyplot as plt
from datetime import date, datetime, timedelta

#session = HTTP("https://api-testnet.bybit.com")

session = HTTP(
    testnet=True,
    api_key="8Iz5xkDJSmGJHy2FCM",
    api_secret="7R7gW18WW4OJzLD0a0ypyPazXXnqqlD0Uf2H",
)

def BTCUSD_MarketData():
	def convert_tuple(tup):
		return ','.join(tup)

	def write_to_file(filename, timestamp):
		with open(filename, 'a') as f:
			f.write(convert_tuple(timestamp))
			f.write('\n')

	#print(session.server_time())  
	#print(session.latest_information_for_symbol(
	#	symbol="BTCUSD"	))

	# Get latest market data
	BTCUSD = session.get_tickers(category="linear", symbol="BTCUSDT")  # returns dictionary
	DATA = BTCUSD['result']['list'][0]  # Access the first item in the list array
	last_price = DATA['lastPrice']
	now = datetime.now()
	date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

	# Save as numbers
	btcusd_timestamp = (str(time()), last_price)
	write_to_file('BTCUSD_f.txt', btcusd_timestamp)

	# Save with date and time
	btcusd_timestamp = (date_time, last_price)
	write_to_file('BTCUSD_dt.txt', btcusd_timestamp)
