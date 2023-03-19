import customtkinter 

class LoginPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        button = customtkinter.CTkButton(self, text="Return",
                           command=lambda: controller.show_frame("StartPage"))
        # Pack the button in the bottom-right corner of the window
        button.pack(side='bottom', anchor='se', padx=10, pady=10)         

        # Add widgets
        label = customtkinter.CTkLabel(self, text="Login", font=("TkDefaultFont", 16))
        label.pack(pady=10)

        # Username field
        username_label = customtkinter.CTkLabel(self, text="Username:")
        username_label.pack()
        self.username_entry = customtkinter.CTkEntry(self)
        self.username_entry.pack()

        # Password field
        password_label = customtkinter.CTkLabel(self, text="Password:")
        password_label.pack()
        self.password_entry = customtkinter.CTkEntry(self, show="*")
        self.password_entry.pack()

        # Login button
        login_button = customtkinter.CTkButton(self, text="Login", command=self.login)
        login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # TODO: Implement login logic here
        if username == "admin" and password == "password":
            self.controller.show_frame("PageOne")
        else:
            # Display error message
            error_label = customtkinter.CTkLabel(self, text="Invalid username or password")
            error_label.pack(pady=10)
