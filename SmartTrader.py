import tkinter as tk
from tkinter.constants import COMMAND
import PyPDF2
from PIL import Image,ImageTk

root = tk.Tk()
root.title('SmartTrader 1.0')
root.iconbitmap('favicon.ico')

class Application:
    def __init__(self, master):
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
        
        #instructions
        self.instructions = tk.Label(master, text='SmartTrader 1.0')
        self.instructions.grid(columnspan=3,column=0,row=1)

        #browse button
        self.browse_text = tk.StringVar()
        self.browse_bin = tk.Button(master, textvariable=self.browse_text, bg="#20bebe", height=2, width=15)
        self.browse_text.set("Ready for Profits?")
        self.browse_bin.grid(column=1,row=2)
        
         
# Run application
app = Application(root)
root.mainloop()