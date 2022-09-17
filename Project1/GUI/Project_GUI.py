
# Creating simple GUI to demostrate SYNC capabilities.

import tkinter
from tkinter import Label, Button, Tk
from PIL import ImageTk, Image
import webbrowser
import shutil
import os

"""
- Square buttons with pictures - Kevin
- Image for background - Kevin

- Create Project button window - Joseph
- Open Porject button window - Joseph

- Home Page - Victor

- Text boxes with text  in (configure pag / create project page) - Mark (Waits on Josephs create project button)

- Save button for (configure page / create project page) - Roberto (Waits on Josephs create project button)
"""

class CAN_BUS_GUI:
    def __init__(self, master) -> None:

        self.master = master
        master.title("First Page")

        # Setting up Texts
        self.label = Label(master, text="CAN BUS")
        self.label.pack()

        # Database Directory Button
        self.File_button_A1 = Button(master, text="Create Project")
        self.File_button_A1.pack()
        self.File_button_A1.place(x=150, y=75)

        # Open Project Button
        self.File_button_A2 = Button(master, text="Open Project")
        self.File_button_A2.pack()
        self.File_button_A2.place(x=525, y=75)

        # Use this for demo purposes...? maybe
    def show_data_base():
        # This function should open a window that show the data base (all .Json files)
        pass
        
    def open_project():
        # This function should prompt a window to select a folder.
        # This function should check that folder to make sure it has: Initial_Config.json & Node_info.json
        # If the function fails go to a first page (Failure would be cant find all json files with that name)
        # If the function passes go to home page
        pass

    def create_project():
        # This function should open a new window with a list of default configurations
        # from the initial_config.json
        # We should have a back button on the new window
        # We should should have a save button that saves the project somewhere
        # This project should then go to home page
        pass



root = Tk()
my_gui = CAN_BUS_GUI(root)
root.geometry("750x500")
root.mainloop()
