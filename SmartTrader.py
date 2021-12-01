import time as time
import tkinter as tk
from tkinter.constants import COMMAND
import PyPDF2
from PIL import Image,ImageTk

root = tk.Tk()
root.title('SmartTrader 1.0')
root.iconbitmap('favicon.ico')


class Application:
    def __init__(self, master):
        tk.Tk.__init__(self, *args, **kwargs)

        #Start Frame
        myFrame = tk.Frame(master)

        self.canvas = tk.Canvas(master,width=600,height=300)
        self.canvas.grid(columnspan=3,rowspan=3)

        #bckgrd logo
        self.file = "coinbase-new4201.jpg"
        self.logo = Image.open(self.file)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(image=self.logo)
        self.logo_label.image_names = self.logo
        self.logo_label.grid(column=1,row=0)
        
        #Enter program button
        self.button_enter = tk.Button(master, text="Start Program", command=lambda:[self.funcA()])
        self.button_enter.grid(column=1,row=1)

        #Exit program button
        self.button_quit = tk.Button(master, text="Exit Program", command=master.quit)
        self.button_quit.grid(column=1,row=2)

    def funcA(self):
        window()

def window():
    tk.Toplevel()
    canvas = tk.Canvas(root, width=600, height=300)
    canvas.grid(columnspan=3,rowspan=3)

# Run application
app = Application(root)

root.mainloop()