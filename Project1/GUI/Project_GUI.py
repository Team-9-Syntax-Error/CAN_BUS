
# Creating simple GUI to demostrate SYNC capabilities.

import tkinter
from tkinter import Label, Button, Tk
from PIL import ImageTk, Image
import webbrowser
import shutil
import os


# TODO: Button for project config
#       Button to view database in finder
#       Button for importing .Json
#       

class CAN_BUS_GUI:
    def __init__(self, master) -> None:

        self.master = master
        master.title("CAN BUS")

        # Setting up Texts
        self.label = Label(master, text="CAN BUS")
        self.label.pack()

        # Read Button Database Directory
        self.File_button_A1 = Button(master, text="Database Directory")
        self.File_button_A1.pack()
        self.File_button_A1.place(x=150, y=75)

        # Read Button Project Configurations
        self.File_button_A2 = Button(master, text="Project Configurations")
        self.File_button_A2.pack()
        self.File_button_A2.place(x=525, y=75)



root = Tk()
my_gui = CAN_BUS_GUI(root)
root.geometry("750x500")
root.mainloop()
