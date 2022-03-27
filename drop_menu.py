# Import module
import cbpro
from requests.auth import AuthBase
from tkinter import *

class CoinbaseWalletAuth(AuthBase):
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

def drop_menu(self):
	# Change the label text
	def show():
		label.config( text = clicked.get() )

	# Dropdown menu options
	options = [
		"Select",
		"Buy",
		"Sell",
		"Limit",
	]

	# datatype of menu text
	clicked = StringVar()

	# initial menu text
	clicked.set( "Select" )

	# Create Dropdown menu
	drop = OptionMenu( self , clicked , *options )
	drop.pack()

	# Create button, it will change label text
	button = Button( self , text = "Confirm" , command = show ).pack()

	# Create Label
	label = Label( self , text = " " )
	label.pack()

	##
	public_client = cbpro.PublicClient()
	#result = public_client.get_product_ticker('BTC-USD')
	result = public_client.get_product_historic_rates('BTC-USD')
	#print(result)

	#api_data = open('Coinbase_ApiKey.txt','r').read().splitlines()
	#passphrase = api_data[0]
	#secret_key = api_data[1]
	#api_key = api_data[2]

	#auth = CoinbaseWalletAuth(api_key,secret_key)
	#auth_client = cbpro.AuthenticatedClient(api_key,secret_key,passphrase)


