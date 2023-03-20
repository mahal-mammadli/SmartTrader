import sys
from tradingview_ta import TA_Handler, Interval
import customtkinter

class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, str):
        self.text_widget.configure(state="normal")
        self.text_widget.insert("end", str)
        self.text_widget.configure(state="disabled")
        self.text_widget.see("end")

def get_tradingview_data(symbol):
    handler = TA_Handler(
    symbol=symbol,
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_MINUTE
    )
    analysis = handler.get_analysis()

    current_price = analysis.summary.get("RECOMMENDATION")
    rsi = analysis.indicators.get("RSI")

    return current_price, rsi
    
class TradingView(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        def submit():
            current_price, rsi = get_tradingview_data(symbol_dropdown.get())
            print(current_price,rsi)

        # Return button
        button = customtkinter.CTkButton(self, text="Return",
                    command=lambda: controller.show_frame("ResearchPage"))
        # Pack the button in the bottom-right corner of the window
        button.pack(side='bottom', anchor='se', padx=10, pady=10)         

        symbol_label = customtkinter.CTkLabel(self, text="Symbol:")
        symbol_label.pack()

        popular_stocks = ["AAPL", "TSLA", "MSFT", "AMZN", "META", "GOOGL", "NFLX", "NVDA", 
                          "PYPL", "DIS", "ADBE", "CRM", "INTC", "CSCO", "AMD", "NVAX", "JPM", "BAC", "GE", "WMT"] 

        symbol_dropdown = customtkinter.CTkOptionMenu(self, values=popular_stocks)
        symbol_dropdown.pack()

        submit_button = customtkinter.CTkButton(self, text="Submit", command=submit)
        submit_button.pack()

        # create console text widget
        self.console_text = customtkinter.CTkTextbox(self, height=10, width=80, state="disabled")
        self.console_text.pack(pady=50, side="bottom", fill="both", expand=True)  # stretch to the sides of the window

        # redirect console output to text widget
        sys.stdout = StdoutRedirector(self.console_text)  
    

