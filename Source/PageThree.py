import os
import customtkinter
import numpy as np

from StartPage import StartPage
from Simulation import Simulation
from Simulation2 import Simulation2

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from pathlib import Path

class WalletFigure():
    fig1 = Figure(figsize=(5,5), dpi=100)
    a1 = fig1.add_subplot(111)

def animate2(i):

    wallet_file = Path("Wallet_List.txt")
    if wallet_file.is_file():
        # file exists
        # path exists
        pullData = open("Wallet_List.txt","r").read()
        dataList = pullData.split('\n')
        xList = []
        yList = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                x,y = eachLine.split(' ')
                xList.append(float(x))
                yList.append(float(y))
        WalletFigure.a1.clear
        WalletFigure.a1.plot(xList,yList)

class PageThree(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        class wallet:
            def __init__(self,total_btc,total_cash):
                self.total_btc = total_btc
                self.total_cash = total_cash

        def enter_click(event):
            x=float(x_entry.get())
            list = open("Sell_x_value_input.txt",'a')
            list.write(str(x))
            list.write('\n')

        def run_Simulation():
            os.system('python Simulation.py')
            my_wallet = Simulation()
            
        def run_Simulation2():
            os.system('python Simulation2.py')
            my_wallet, moving_averages, iteration_ma, above_or_below, above_or_below_percent = Simulation2()
            plt.plot(iteration_ma,moving_averages)
            plt.title('Simulation2 Moving Average')
            plt.legend()
            plt.show()

            plt.plot(iteration_ma,above_or_below)
            plt.title('Simulation2 Moving Average A OR B')
            plt.legend()
            plt.show()

            plt.plot(iteration_ma,above_or_below_percent)
            plt.title('Simulation2 Moving Average A OR B %')
            plt.legend()
            plt.show()        

            counts, bins = np.histogram(above_or_below_percent)
            plt.stairs(counts, bins)
            plt.legend()
            plt.show()    
            
            
        self.controller = controller
        label = customtkinter.CTkLabel(self, text="Smart Trader", font=customtkinter.CTkFont(size=20, weight="bold"))
        label.pack(padx=20, pady=(30,2))
        label = customtkinter.CTkLabel(self, text="Trading Simulator", font=customtkinter.CTkFont(size=18, weight="normal"))
        label.pack()

        # Tool Menu Options
        button1 = customtkinter.CTkButton(self, text="Research",
                           command=lambda: controller.show_frame("ResearchPage"))                         
        button2 = customtkinter.CTkButton(self, text="Trading Simulator",
                           command=lambda: controller.show_frame("PageThree"), bg_color='blue', fg_color='blue') 
        button3 = customtkinter.CTkButton(self,text="Trading Bot",
                           command=lambda: controller.show_frame("PageFour"))                                    
        button1.pack(anchor='nw', pady=10)
        button2.pack(anchor='nw', pady=10)
        button3.pack(anchor='nw', pady=10)   

        # Simulation Settings
        SimSettingsFrame = customtkinter.CTkFrame(self)
        SimSettingsFrame.pack(side='left', fill='x')

        label = customtkinter.CTkLabel(SimSettingsFrame, text="Simulation Settings", font=customtkinter.CTkFont(size=12, weight="normal"))
        label.pack(padx=5, pady=10)
                           
        label = customtkinter.CTkLabel(SimSettingsFrame, text="Enter sell x value:")
        label.pack(padx=10, pady=10)
        x_entry = customtkinter.CTkEntry(SimSettingsFrame)
        x_entry.pack(padx=10, pady=10)
        enter_button = customtkinter.CTkButton(SimSettingsFrame, text="Enter")
        enter_button.pack(padx=10, pady=10)
        enter_button.bind("<Button-1>", enter_click)
        enter_button.bind("<Return>", enter_click)
        
        # Simulation Strategies
        button1 = customtkinter.CTkButton(SimSettingsFrame, text='Run Simulation', command=run_Simulation)
        button2 = customtkinter.CTkButton(SimSettingsFrame, text='Run Simulation 2', command=run_Simulation2)
        button1.pack(padx=10, pady=10)
        button2.pack(padx=10, pady=10)

        # Return button
        button = customtkinter.CTkButton(self, text="Return",
                           command=lambda: controller.show_frame("MenuPage"))
        # Pack the button in the bottom-right corner of the window
        button.pack(side='bottom', anchor='se', padx=10, pady=10)
        

        # Wallet Graph
        canvas = FigureCanvasTkAgg(WalletFigure.fig1, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=customtkinter.LEFT, fill=customtkinter.NONE, expand=True)   

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=True)