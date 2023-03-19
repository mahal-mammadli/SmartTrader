import customtkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from ByBit_MarketData import BTCUSD_MarketData
from matplotlib.figure import Figure

# Use the 'ggplot' style sheet
plt.style.use('seaborn-whitegrid')

class BtcFigure:
    f, axes = plt.subplots(figsize=(5, 5), dpi=100)

def animate(i):
    with open("BTCUSD_f.txt", "r") as data_file:
        data_list = data_file.read().split('\n')
        x_list = []
        y_list = []
        for each_line in data_list:
            if len(each_line) > 1:
                x, y = each_line.split(',')
                x_list.append(float(x))
                y_list.append(float(y))
        BtcFigure.axes.clear()
        BtcFigure.axes.plot(x_list, y_list)
        BtcFigure.axes.set_title('BTC-USD')
        BtcFigure.axes.set_ylabel('USD')

class PageTwo(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = customtkinter.CTkLabel(self, text="Smart Trader", font=customtkinter.CTkFont(size=20, weight="bold"))
        label.pack(padx=20, pady=30)
        button = customtkinter.CTkButton(self, text="Return", command=lambda: controller.show_frame("PageOne"))
        # Pack the button in the bottom-right corner of the window
        button.pack(side='bottom', anchor='se', padx=10, pady=10) 

        canvas = FigureCanvasTkAgg(BtcFigure.f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=True)
        self.update_market_data()
        
    def update_market_data(self):
        BTCUSD_MarketData()
        self.after(1000, self.update_market_data)