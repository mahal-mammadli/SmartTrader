import os
import customtkinter

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from ByBit_MarketData import BTCUSD_MarketData

class BtcFigure():
    f = Figure(figsize=(5,5), dpi=100)
    a = f.add_subplot(111)

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
    BtcFigure.a.clear
    BtcFigure.a.plot(xList,yList)

class PageTwo(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = customtkinter.CTkLabel(self, text="BTC USD Price")
        label.pack(side="top", fill="x", pady=10)
        button = customtkinter.CTkButton(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

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