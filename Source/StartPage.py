import os
import sys
import customtkinter

from PageOne import PageOne


class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, str):
        self.text_widget.configure(state="normal")
        self.text_widget.insert("end", str)
        self.text_widget.configure(state="disabled")
        self.text_widget.see("end")


class StartPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        # create console text widget
        self.console_text = customtkinter.CTkTextbox(self, height=10, width=80, state="disabled")
        self.console_text.pack(pady=50, side="bottom", fill="both", expand=True)  # stretch to the sides of the window

        # redirect console output to text widget
        sys.stdout = StdoutRedirector(self.console_text)                

        self.logo_label = customtkinter.CTkLabel(self, text="Smart Trader", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(padx=20, pady=30)
        self.sidebar_start_button = customtkinter.CTkButton(self, command=lambda: controller.show_frame("LoginPage"), text="Start")
        self.sidebar_start_button.pack(padx=20, pady=(20,10))

        self.sidebar_exit_button = customtkinter.CTkButton(self, command=self.exit, text="Exit")
        self.sidebar_exit_button.pack(padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.pack(padx=20, pady=(100,10))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.pack(padx=20, pady=10)
        self.scaling_label = customtkinter.CTkLabel(self, text="UI Scaling:", anchor="w")
        self.scaling_label.pack(padx=20, pady=10)
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.pack(padx=20, pady=10)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def exit(self):
        # remove files if they exist
        for file_name in [
            "Buy_List.txt",
            "Sell_List.txt",
            "Sell_x_value_input.txt",
            "Wallet_List.txt",
            "BTCUSD_dt.txt",
            "BTCUSD_f.txt",
        ]:
            if os.path.isfile(file_name):
                os.remove(file_name)

        self.quit()