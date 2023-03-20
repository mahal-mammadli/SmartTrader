import os
import customtkinter
from customtkinter import *

from StartPage import StartPage
from SpotBuySell import spot_buy_sell_transaction, fetchWalletBalance

class PageFour(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = customtkinter.CTkLabel(self, text="Smart Trader", font=customtkinter.CTkFont(size=20, weight="bold"))
        label.pack(padx=20, pady=(30,2))
        label = customtkinter.CTkLabel(self, text="Trading Bot", font=customtkinter.CTkFont(size=18, weight="normal"))
        label.pack()

        button = customtkinter.CTkButton(self, text="Return",
                           command=lambda: controller.show_frame("MenuPage"))
        
        # Pack the button in the bottom-right corner of the window
        button.pack(side='bottom', anchor='se', padx=10, pady=10)

        # Tool Menu Options
        button1 = customtkinter.CTkButton(self, text="Research",
                           command=lambda: controller.show_frame("ResearchPage"))                         
        button2 = customtkinter.CTkButton(self, text="Trading Simulator",
                           command=lambda: controller.show_frame("PageThree")) 
        button3 = customtkinter.CTkButton(self,text="Trading Bot",
                           command=lambda: controller.show_frame("PageFour"), bg_color='blue', fg_color='blue')                                    
        button1.pack(anchor='nw', pady=10)
        button2.pack(anchor='nw', pady=10)
        button3.pack(anchor='nw', pady=10)    

        # Available Balance Figure
        BalanceFigure = customtkinter.CTkFrame(self)
        BalanceFigure.pack(side='left', fill='x', expand=TRUE)

        label = customtkinter.CTkLabel(BalanceFigure, text="Total Balances", font=customtkinter.CTkFont(size=12, weight="bold"))
        label.pack(pady=20)        

        balance = fetchWalletBalance()
        self.coinTotal_labels = []
        for i in range(0,len(balance['result']['balances'])):
            coinId = balance['result']['balances'][i]['coinId']
            coin_total = balance['result']['balances'][i]['total'] 
            label = customtkinter.CTkLabel(BalanceFigure, text=coinId+" : "+coin_total)
            label.pack()
            self.coinTotal_labels.append(label)

        self.updateDisplay()

	    # Spot Buy Options
        SpotBuyFrame = customtkinter.CTkFrame(self)
        SpotBuyFrame.pack(side='right', fill='x', expand=TRUE)

        label = customtkinter.CTkLabel(SpotBuyFrame, text="Spot Buy and Sell", font=customtkinter.CTkFont(size=12, weight="bold"))
        label.pack(pady=10)   

        self.clicked = StringVar()
        self.clicked.set("Buy")
        self.clicked2= StringVar()
        self.clicked2.set("ETHUSDT")
        drop = customtkinter.CTkOptionMenu( SpotBuyFrame , values=["Buy", "Sell"],
		    command=self.update_transaction_cmd)
        drop.pack(padx=10,pady=10)
        drop2 = customtkinter.CTkOptionMenu( SpotBuyFrame, values=["ETHUSDT", "BTCUSDT"],
            command=self.update_transaction_coin)
        drop2.pack(padx=10,pady=10)

        #Buy
        qty = customtkinter.CTkLabel(SpotBuyFrame, text="Enter buy quantity [ USDT ]")
        qty.pack(padx=10,pady=2)
        qty_entry = customtkinter.CTkEntry(SpotBuyFrame)
        qty_entry.pack(padx=10,pady=5)
	    #Sell
        qty2 = customtkinter.CTkLabel(SpotBuyFrame, text="Enter sell quantity")
        qty2.pack(padx=10,pady=2)
        qty_entry2 = customtkinter.CTkEntry(SpotBuyFrame)
        qty_entry2.pack(padx=10,pady=5)

        def call_spot_buy_sell_transaction():
            result = spot_buy_sell_transaction(self.clicked, self.clicked2, qty_entry, qty_entry2)
            label = customtkinter.CTkLabel( SpotBuyFrame , text = result )
            label.pack()

        # Create button, it will change label text
        button = customtkinter.CTkButton( SpotBuyFrame , text = "Execute" , command = call_spot_buy_sell_transaction ).pack(padx=10,pady=5)

        # Create Label
        label = customtkinter.CTkLabel( self , text = " " )
        label.pack()      

    def update_transaction_cmd(self, option: str):
        self.clicked.set(option)

    def update_transaction_coin(self, option2: str):
        self.clicked2.set(option2)
   
    def updateDisplay(self):
        balance = fetchWalletBalance()
        for i in range(0,len(balance['result']['balances'])):
            coinId = balance['result']['balances'][i]['coinId']
            coin_total = balance['result']['balances'][i]['total'] 
            self.coinTotal_labels[i].configure(text=coinId+" : "+coin_total)
        self.after(10000, self.updateDisplay)