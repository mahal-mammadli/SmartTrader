import os
import customtkinter
from customtkinter import *

from StartPage import StartPage
from SpotBuySell import spot_buy_sell_transaction, fetchWalletBalance

class PageFour(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = customtkinter.CTkLabel(self, text="ProTrader Bot 1.0")
        label.pack(side="top", fill="x", pady=10)
        button = customtkinter.CTkButton(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        session, balance = fetchWalletBalance()
        coinId_labels = []
        self.coinTotal_labels = []
        for i in range(0,len(balance['result']['balances'])):
            coinId = balance['result']['balances'][i]['coinId']
            coin_total = balance['result']['balances'][i]['total'] 
            label = customtkinter.CTkLabel(self, text="Available Balance "+coinId+":")
            label.pack()
            coinId_labels.append(label)
            label = customtkinter.CTkLabel(self, text=coin_total)      
            label.pack()
            self.coinTotal_labels.append(label)

        self.updateDisplay()

	    # Create Dropdown menu
        self.clicked = StringVar()
        self.clicked.set("Buy")
        self.clicked2= StringVar()
        self.clicked2.set("ETHUSDT")
        drop = customtkinter.CTkOptionMenu( self , values=["Buy", "Sell"],
		    command=self.update_transaction_cmd)
        drop.pack()
        drop2 = customtkinter.CTkOptionMenu( self, values=["ETHUSDT", "BTCUSDT"],
            command=self.update_transaction_coin)
        drop2.pack()

        #Buy
        qty = customtkinter.CTkLabel(self, text="Enter buy quantity [USDT]:")
        qty.pack()
        qty_entry = customtkinter.CTkEntry(self)
        qty_entry.pack()
	    #Sell
        qty2 = customtkinter.CTkLabel(self, text="Enter sell quantity:")
        qty2.pack()
        qty_entry2 = customtkinter.CTkEntry(self)
        qty_entry2.pack()

        def call_spot_buy_sell_transaction():
            result = spot_buy_sell_transaction(self.clicked, self.clicked2, qty_entry, qty_entry2)
            label = customtkinter.CTkLabel( self , text = result )
            label.pack()

        # Create button, it will change label text
        button = customtkinter.CTkButton( self , text = "Execute" , command = call_spot_buy_sell_transaction ).pack()

        # Create Label
        label = customtkinter.CTkLabel( self , text = " " )
        label.pack()        

    def update_transaction_cmd(self, option: str):
        self.clicked.set(option)

    def update_transaction_coin(self, option2: str):
        self.clicked2.set(option2)
   
    def updateDisplay(self):
        session, balance = fetchWalletBalance()
        for i in range(0,len(balance['result']['balances'])):
            coinId = balance['result']['balances'][i]['coinId']
            coin_total = balance['result']['balances'][i]['total'] 
            self.coinTotal_labels[i].configure(text = coin_total)
        self.after(10000, self.updateDisplay)