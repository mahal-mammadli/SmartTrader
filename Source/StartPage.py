import os
import sys
import customtkinter

class StartPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.logo_label = customtkinter.CTkLabel(self, text="Smart Trader", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(padx=20, pady=30)

        # Username field
        username_label = customtkinter.CTkLabel(self, text="ID", font=customtkinter.CTkFont(size=10, weight="bold"))
        username_label.pack(pady=2)
        self.username_entry = customtkinter.CTkEntry(self)
        self.username_entry.pack()

        # Password field
        password_label = customtkinter.CTkLabel(self, text="Password", font=customtkinter.CTkFont(size=10, weight="bold"))
        password_label.pack(pady=2)
        self.password_entry = customtkinter.CTkEntry(self, show="*")
        self.password_entry.pack()

        # Login button
        login_button = customtkinter.CTkButton(self, text="Login", command=self.login)
        login_button.pack(pady=10)

        self.sidebar_exit_button = customtkinter.CTkButton(self, command=self.exit, text="Exit")
        self.sidebar_exit_button.pack(padx=20, pady=10)

        # Create a new frame to hold the appearance mode and scaling options
        options_frame = customtkinter.CTkFrame(self)
        options_frame.pack(side="bottom", fill="x", padx=20, pady=(100, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(options_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.pack(side='left', anchor='sw', padx=20, pady=10)
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(options_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.pack(side='left', anchor='sw', padx=20)
        self.scaling_label = customtkinter.CTkLabel(options_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.pack(side='left', anchor='sw', padx=20, pady=10)
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(options_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.pack(side='left', anchor='sw', padx=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # TODO: Implement login logic here
        if username == "admin" and password == "password":
            self.controller.show_frame("MenuPage")
        else:
            # Display error message
            error_label = customtkinter.CTkLabel(self, text="Invalid username or password")
            error_label.pack(pady=10)
            

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