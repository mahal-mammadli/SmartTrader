import os
import customtkinter

class PageOne(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = customtkinter.CTkLabel(self, text="ProTrader Bot 1.0")
        label.pack(side="top", fill="x", pady=10)
        button = customtkinter.CTkButton(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button1 = customtkinter.CTkButton(self, text="BTC USD Live Chart",
                           command=lambda: controller.show_frame("PageTwo"))
        button2 = customtkinter.CTkButton(self, text="Trading Bot Simulator",
                           command=lambda: controller.show_frame("PageThree")) 
        button3 = customtkinter.CTkButton(self,text="Trading Bot",
                           command=lambda: controller.show_frame("PageFour"))                                      
        button.pack()
        button1.pack()
        button2.pack()
        button3.pack()