import os
import customtkinter

from PageOne import PageOne

class StartPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.logo_label = customtkinter.CTkLabel(self, text="Smart Trader", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_start_button = customtkinter.CTkButton(self, command=lambda: controller.show_frame("PageOne"), text="Start")
        self.sidebar_start_button.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_exit_button = customtkinter.CTkButton(self, command=self.exit, text="Exit")
        self.sidebar_exit_button.grid(row=2, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def exit(self):
        if (os.path.isfile("Buy_List.txt")):
            os.remove("Buy_List.txt")    
        if (os.path.isfile("Sell_List.txt")):
            os.remove("Sell_List.txt")
        if (os.path.isfile("Sell_x_value_input.txt")):
            os.remove("Sell_x_value_input.txt")
        if (os.path.isfile("Wallet_List.txt")):
            os.remove("Wallet_List.txt")
        if (os.path.isfile("BTCUSD_dt.txt")):
            os.remove("BTCUSD_dt.txt")
        if (os.path.isfile("BTCUSD_f.txt")):
            os.remove("BTCUSD_f.txt")
        self.quit()