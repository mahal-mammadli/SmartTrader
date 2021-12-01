from pybit import HTTP
from matplotlib import pyplot as plt
from datetime import datetime

# Python3 program to Convert a
# list to dictionary

def Convert(a):
	it = iter(a)
	res_dct = dict(zip(it, it))
	return res_dct
		
session = HTTP("https://api-testnet.bybit.com")
print(session.server_time())  
print(session.latest_information_for_symbol(
    symbol="BTCUSD"
))

BTCUSD = session.latest_information_for_symbol(symbol="BTCUSD") #returns dictionary
DATA = BTCUSD['result']
last_price = DATA[0]['last_price']
now = datetime.now()
utc_datetime = datetime.utcnow()

time_btcusd_price_list = open('BTCUSD.txt',"w")

#print(last_price,now)
#plt.plot(now,last_price)


