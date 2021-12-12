# Import module
from tkinter import *

# Create object
#root = Tk()

# Adjust size
#root.geometry( "200x200" )

def drop_menu(self):
	# Change the label text
	def show():
		label.config( text = clicked.get() )

	# Dropdown menu options
	options = [
		"Select",
		"Buy",
		"Sell",
		"Limit",
	]

	# datatype of menu text
	clicked = StringVar()

	# initial menu text
	clicked.set( "Select" )

	# Create Dropdown menu
	drop = OptionMenu( self , clicked , *options )
	drop.pack()

	# Create button, it will change label text
	button = Button( self , text = "Confirm" , command = show ).pack()

	# Create Label
	label = Label( self , text = " " )
	label.pack()

# Execute tkinter
# root.mainloop()#
