# Import module
import bybit
import time
import matplotlib
from customtkinter import *
from pybit.unified_trading import HTTP

from ConfigKey import ConfigKey

import requests

response = requests.get("https://ipinfo.io/json")
print(response.json())

session = HTTP(
    api_key=ConfigKey.api_key,
    api_secret=ConfigKey.api_secret
)
if session:
	print('Logged in to ByBit API.')	

def spot_buy_sell_transaction(clicked, clicked2, qty_entry, qty_entry2):
	balance = fetchWalletBalance()
	# Dropdown menu options
	options = [
		"Select",
		"Buy",
		"Sell",
	]

	coinOptions = [
		"Select",
		"ETHUSDT",
		"BTCUSDT",
	]	
	result = 'Trade not executed.'
	selected_option = clicked.get()
	selected_coin = clicked2.get()
	if (qty_entry.get()):
		buy_qty=(float(qty_entry.get()))
		if ('Buy' == selected_option and buy_qty > 0):
			result = session.place_active_order(
   			symbol=selected_coin,
   			qty=buy_qty,				
   			side="Buy",
   			type="Market",
   			time_in_force="GoodTillCancel"
			)
			print(result)
			if (result['ret_msg'] == 'OK'):
				result = 'Trade succesfully completed.'
				print('Trade succesfully completed.')
			else:
				result = 'Trade unsuccesful.'
				print('Trade unsuccessful.')
	if (qty_entry2.get()):
		sell_qty = (float(qty_entry2.get()))
		if ('Sell' == selected_option and sell_qty > 0):
			result = session.place_active_order(
   			symbol=selected_coin,
   			qty=sell_qty,				
   			side="Sell",
   			type="Market",
   			time_in_force="GoodTillCancel"
			)
			print(result)
			if (result['ret_msg'] == 'OK'):
				result = 'Trade succesfully completed.'
				print('Trade succesfully completed.')
			else:
				result = 'Trade unsuccesful.'
				print('Trade unsuccessful.')
	return result

def fetchWalletBalance():
	# We can fetch our wallet balance using an auth'd session.
	#balance = session.get_wallet_balance()
	balance = 0
	#print(balance)

	return balance

