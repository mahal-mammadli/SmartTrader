import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import customtkinter
from tkcalendar import DateEntry

from PageOne import PageOne

# Create a figure and a subplot
fig = plt.figure()
ax = fig.add_subplot(111)

class PageFive(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller
        label = customtkinter.CTkLabel(self, text="Smart Trader", font=customtkinter.CTkFont(size=20, weight="bold"))
        label.pack(padx=20, pady=30)
        label = customtkinter.CTkLabel(self, text="BTC-USD Historical Data", font=customtkinter.CTkFont(size=16, weight="bold"))
        label.pack(padx=5, pady=5)        
        button = customtkinter.CTkButton(self, text="Return",
                command=lambda: controller.show_frame("PageOne"))
        # Pack the button in the bottom-right corner of the window
        button.pack(side='bottom', anchor='se', padx=10, pady=10)         

        # Create a function to make the API request and plot the data
        def plot_data():
            # Set the API endpoint URL
            api_url = 'https://api.coindesk.com/v1/bpi/historical/close.json'

            # Get the start and end dates from the user input fields
            start_date = start_date_entry.get_date()
            end_date = end_date_entry.get_date()
        
            # Convert the date objects to string format
            start_date_str = start_date.strftime('%Y-%m-%d')
            end_date_str = end_date.strftime('%Y-%m-%d')

            # Set the parameters for the API request
            params = {'start': start_date_str, 'end': end_date_str}

            # Make the GET request to the API
            response = requests.get(api_url, params=params)

                # Check the status code of the response to make sure the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()
                # Get the average price for the specified date range
                prices = data['bpi']

                # Create a list of dates and a list of prices
                dates = []
                y_values = []
                for date, price in prices.items():
                    dates.append(date)
                    y_values.append(price)

                # Plot the data on the subplot
                ax.clear()
                ax.plot(dates, y_values)
                ax.set_xlabel('Date')
                ax.set_ylabel('Price (USD)')
                ax.set_title('Average Price of Bitcoin')
                ax.set_xticklabels(dates, rotation=60)
                ax.tick_params(axis='x', labelsize=5)

                # Update the plot
                fig.canvas.draw()
            else:
                # If the request was not successful, print the status code
                print(f'Request failed with status code {response.status_code}')

        # Create the side frame
        SideFrame = customtkinter.CTkFrame(self)
        SideFrame.pack(side='left', fill='x', expand=True)

        # Create the start date input field
        start_date_label = customtkinter.CTkLabel(SideFrame, text='Start Date:')
        start_date_label.pack(padx=10, pady=10, expand=True)
        start_date_entry = DateEntry(SideFrame, width=12, background='darkblue',
                             foreground='white', borderwidth=2)
        start_date_entry.pack(padx=10, pady=10, expand=True)

        # Create the end date input field
        end_date_label = customtkinter.CTkLabel(SideFrame, text='End Date:')
        end_date_label.pack(padx=10, pady=10, expand=True)
        end_date_entry = DateEntry(SideFrame, width=12, background='darkblue',
                           foreground='white', borderwidth=2)
        end_date_entry.pack(padx=10, pady=10, expand=True)

        # Create a button to plot the data
        plot_button = customtkinter.CTkButton(SideFrame, text='Plot Data', command=plot_data)
        plot_button.pack(padx=10, pady=10, expand=True)

        # Create a canvas to display the plot
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.get_tk_widget().pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=True, pady=5)
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=True, pady=2)