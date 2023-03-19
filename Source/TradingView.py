import sys
from tradingview_ta import TA_Handler, Interval
import customtkinter
from yahoo_fin.stock_info import get_day_most_active
from StartPage import StdoutRedirector

def get_tradingview_data(symbol):
    handler = TA_Handler(
        symbol=symbol,
        screener="america",
        exchange="NASDAQ",
        interval=Interval.INTERVAL_1_MINUTE
    )
    return handler.get_analysis()

class TradingView(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        def submit():
            analysis = get_tradingview_data(symbol_dropdown.get())
            current_price = analysis.summary.get("RECOMMENDATION")
            rsi = analysis.indicators.get("RSI")
            print(current_price, rsi)

        # Return button
        button = customtkinter.CTkButton(self, text="Return",
                    command=lambda: controller.show_frame("PageOne"))
        # Pack the button in the bottom-right corner of the window
        button.pack(side='bottom', anchor='se', padx=10, pady=10)         

        symbol_label = customtkinter.CTkLabel(self, text="Symbol:")
        symbol_label.pack()

        # Get the list of stocks sorted by market cap
        top_stocks = get_day_most_active()
        popular_stocks = list(top_stocks[:10].Symbol)

        symbol_dropdown = customtkinter.CTkOptionMenu(self, values=popular_stocks)
        symbol_dropdown.pack()

        submit_button = customtkinter.CTkButton(self, text="Submit", command=submit)
        submit_button.pack()

        # create console text widget
        self.console_text = customtkinter.CTkTextbox(self, height=10, width=80, state="disabled")
        self.console_text.pack(pady=50, side="bottom", fill="both", expand=True)  # stretch to the sides of the window

        # redirect console output to text widget
        sys.stdout = StdoutRedirector(self.console_text)
