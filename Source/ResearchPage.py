import os
import customtkinter

class ResearchPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = customtkinter.CTkLabel(self, text="Smart Trader", font=customtkinter.CTkFont(size=20, weight="bold"))
        label.pack(padx=20, pady=(30,2))
        label = customtkinter.CTkLabel(self, text="Research Tools", font=customtkinter.CTkFont(size=18, weight="normal"))
        label.pack()

        # Tool Menu Options
        button1 = customtkinter.CTkButton(self, text="Research",
                           command=lambda: controller.show_frame("ResearchPage"), bg_color='blue', fg_color='blue')                         
        button2 = customtkinter.CTkButton(self, text="Trading Simulator",
                           command=lambda: controller.show_frame("PageThree")) 
        button3 = customtkinter.CTkButton(self,text="Trading Bot",
                           command=lambda: controller.show_frame("PageFour"))                                    
        button1.pack(anchor='nw', pady=10)
        button2.pack(anchor='nw', pady=10)
        button3.pack(anchor='nw', pady=10) 

        # Research tool menu options
        button4 = customtkinter.CTkButton(self, text="BTC USD Live Chart",
                           command=lambda: controller.show_frame("PageTwo"))
        button5 = customtkinter.CTkButton(self,text="View BTC-USD Historical Data",
                           command=lambda: controller.show_frame("PageFive"))                           
        button6 = customtkinter.CTkButton(self,text="ChatGPT",
                           command=lambda: controller.show_frame("ChatGPT"))
        button7 = customtkinter.CTkButton(self,text="TradingView",
                           command=lambda: controller.show_frame("TradingView"))                                           
        button4.pack(pady=10)
        button5.pack(pady=10)
        button6.pack(pady=10)
        button7.pack(pady=10)

        button = customtkinter.CTkButton(self, text="Log out",
            command=lambda: controller.show_frame("StartPage"))
        # Pack the button in the bottom-right corner of the window
        button.pack(side='bottom', anchor='se', padx=10, pady=10)





   