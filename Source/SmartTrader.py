import tkinter
import tkinter.messagebox
import customtkinter
import os

#
from StartPage import StartPage
from LoginPage import LoginPage
from PageOne import PageOne
from PageTwo import PageTwo, BtcFigure, animate
from PageThree import PageThree, WalletFigure, animate2
from PageFour import PageFour
from PageFive import PageFive
from ChatGPT import ChatGPT
from TradingView import TradingView

import matplotlib.animation as animation

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Smart Trader 1.0")
        self.geometry(f"{800}x{700}")
        
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, LoginPage, PageOne, PageTwo, PageThree, PageFour, PageFive, ChatGPT,
                  TradingView):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()                

if __name__ == "__main__":
    app = App()
    ani = animation.FuncAnimation(BtcFigure.f, animate, interval=1000)
    ani2 = animation.FuncAnimation(WalletFigure.fig1, animate2, interval=1000)
    app.mainloop()