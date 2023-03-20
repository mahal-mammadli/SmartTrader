import openai
import customtkinter
from ConfigKey import ConfigKey

class ChatGPT(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        # Return button
        button = customtkinter.CTkButton(self, text="Return",
                    command=lambda: controller.show_frame("ResearchPage"))
        # Pack the button in the bottom-right corner of the window
        button.pack(side='bottom', anchor='se', padx=10, pady=10) 

        # Set up the OpenAI API client
        openai.api_key = ConfigKey.openai_secret

        # Create the side frame
        SideFrame = customtkinter.CTkFrame(self)
        SideFrame.pack(side='left', fill='x', expand=True)

        # Create a label for the chat history
        self.chat_history_label = customtkinter.CTkLabel(SideFrame, text='Chat History')
        self.chat_history_label.pack(side='top', padx=10, pady=10, fill='x')

        # Create a text widget to display the chat history
        self.chat_history_text = customtkinter.CTkTextbox(SideFrame, state='disabled')
        self.chat_history_text.pack(side='top', padx=10, pady=10, fill='both', expand=True)

        # Create a button to submit the user input
        self.submit_button = customtkinter.CTkButton(SideFrame, text='Submit', command=self.generate_response)
        self.submit_button.pack(side='right', padx=5, pady=10)

        # Create an entry widget for the user input
        self.user_input_entry = customtkinter.CTkEntry(SideFrame)
        self.user_input_entry.pack(side='bottom', padx=10, pady=10, fill='both', expand=True)

        # Define the default prompt for generating text
        self.prompt = ''

        # Set the model and parameters for generating text
        self.model_engine = "text-davinci-003"
        self.params = {
            "prompt": self.prompt,
            "temperature": 0.5,
            "max_tokens": 50,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }

    def generate_response(self):
        # Get the user input from the entry widget
        user_input = self.user_input_entry.get()

        # Display the user input in the chat history
        self.chat_history_text.configure(state='normal')
        self.chat_history_text.insert(customtkinter.END, 'User: ' + user_input + '\n')

        # Set the prompt for generating text
        self.params['prompt'] = self.prompt + ' ' + user_input

        # Send the API request to generate text
        response = openai.Completion.create(engine=self.model_engine, prompt=self.params['prompt'], max_tokens=self.params['max_tokens'])

        # Parse the response and extract the generated text
        generated_text = response.choices[0].text.strip()

        # Display the generated text in the chat history
        self.chat_history_text.insert(customtkinter.END, 'ChatGPT: ' + generated_text + '\n')
        self.chat_history_text.configure(state='disabled')

        # Clear the user input entry widget
        self.user_input_entry.delete(0, customtkinter.END)
