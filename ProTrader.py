import tkinter as tk                # python 3
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.pyplot import fill
from tkinter import font as tkfont  # python 3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

from ByBit_MarketData import BTCUSD_MarketData

style.use("dark_background") #"ggplot"

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
    a.clear
    a.plot(xList,yList)


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("ProTrader 1.0")
        self.iconbitmap('favicon.ico')

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pro Trader 1.0", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Start",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.quit())
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="ProTrader Bot 1.0", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1 = tk.Button(self, text="BTC USD Live Chart",
                           command=lambda: controller.show_frame("PageTwo"))
        button2 = tk.Button(self, text="Trading Bot",
                           command=lambda: controller.show_frame("PageThree"))                                        
        button.pack()
        button1.pack()
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="BTC USD Price", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.update_MarketData()

    def update_MarketData(self):
        BTCUSD_MarketData()
        self.after(1000, self.update_MarketData)
        
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Trading Bot 1.0", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1 = tk.Button(self, text='Run Simulation')
                  
        button.pack()
        button1.pack()

if __name__ == "__main__":
    app = SampleApp()
    ani = animation.FuncAnimation(f, animate, interval=1000)
    app.mainloop()