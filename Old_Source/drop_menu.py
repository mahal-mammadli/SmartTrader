# Import module
import bybit
import time
import matplotlib
from requests.auth import AuthBase
from tkinter import *
from pybit import inverse_perpetual  # <-- import HTTP & WSS for inverse perp
from pybit import spot

class CoinbaseWalletAuth(AuthBase):
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

def drop_menu(self):
	def spot_buy():
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
		label.config(text=result)
	# Change the label text
	def show():
		#label.config( text = clicked.get() )
		spot_buy()

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

	# datatype of menu text
	clicked = StringVar()
	clicked2 = StringVar()

	# initial menu text
	clicked.set( "Select" )
	clicked2.set( "Select" )

	# Create Dropdown menu
	drop = OptionMenu( self , clicked , *options )
	drop.pack()

	drop2 = OptionMenu( self, clicked2, *coinOptions)
	drop2.pack()

	# Create button, it will change label text
	button = Button( self , text = "Confirm" , command = show ).pack()

	# Create Label
	label = Label( self , text = " " )
	label.pack()
	
	#Buy
	qty = Label(self, text="Enter buy quantity [USDT]:")
	qty.pack()
	qty_entry = Entry(self)
	qty_entry.pack()
	#Sell
	qty2 = Label(self, text="Enter sell quantity ["+clicked2.get()+"]:")
	qty2.pack()
	qty_entry2 = Entry(self)
	qty_entry2.pack()
    # ByBit Testing1 API
	api_key = "ZY7E0KBm4gstFsegIp"
	api_secret = "qqnqEdpt4tX3AFlmuUQBkKUA0M0E7N0Sn78K"

	#client = bybit.bybit(test=False, api_key = api_key, api_secret = api_secret)
	session = spot.HTTP(
    	endpoint='https://api.bybit.com', 
    	api_key=api_key,
    	api_secret=api_secret
	)
	print('Logged in.')
	# We can fetch our wallet balance using an auth'd session.
	balance = session.get_wallet_balance()
	print(balance)
	print(balance['result']['balances'])
	coinId = balance['result']['balances'][0]['coinId']
	coin_total = balance['result']['balances'][0]['total']
	return coinId, coin_total