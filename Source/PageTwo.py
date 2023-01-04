import os
import customtkinter

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from ByBit_MarketData import BTCUSD_MarketData
import matplotlib.pyplot as plt

# Use the 'ggplot' style sheet
plt.style.use('seaborn-whitegrid')

class BtcFigure():

    f = Figure(figsize=(5,5), dpi=100)
    axes = f.add_subplot(111)

def animate(i):
    pullData = open("BTCUSD_f.txt","r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x,y = eachLine.split(',')
            xList.append(float(x))
            yList.append(float(y))
    BtcFigure.axes.clear
    BtcFigure.axes.plot(xList,yList)
    BtcFigure.axes.set_title('BTC-USD')
    BtcFigure.axes.set_ylabel('USD')

class PageTwo(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = customtkinter.CTkLabel(self, text="Smart Trader", font=customtkinter.CTkFont(size=20, weight="bold"))
        label.pack(padx=20, pady=30)
        button = customtkinter.CTkButton(self, text="Return",
                           command=lambda: controller.show_frame("PageOne"))
        # Pack the button in the bottom-right corner of the window
        button.pack(side='bottom', anchor='se', padx=10, pady=10) 
         
        canvas = FigureCanvasTkAgg(BtcFigure.f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=True)
        self.update_MarketData()
        
    def update_MarketData(self):
        BTCUSD_MarketData()
        self.after(1000, self.update_MarketData)