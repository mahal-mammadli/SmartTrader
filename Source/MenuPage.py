import os
import customtkinter

class MenuPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = customtkinter.CTkLabel(self, text="Smart Trader", font=customtkinter.CTkFont(size=20, weight="bold"))
        label.pack(padx=20, pady=30)
        button1 = customtkinter.CTkButton(self, text="Research",
                           command=lambda: controller.show_frame("ResearchPage"))                         
        button2 = customtkinter.CTkButton(self, text="Trading Simulator",
                           command=lambda: controller.show_frame("PageThree")) 
        button3 = customtkinter.CTkButton(self,text="Trading Bot",
                           command=lambda: controller.show_frame("PageFour"))                                    
        button1.pack(pady=10)
        button2.pack(pady=10)
        button3.pack(pady=10)

        button = customtkinter.CTkButton(self, text="Return",
            command=lambda: controller.show_frame("StartPage"))
        # Pack the button in the bottom-right corner of the window
        button.pack(side='bottom', anchor='se', padx=10, pady=10)





   