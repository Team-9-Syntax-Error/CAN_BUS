
from tkinter import Label, Button, Tk, Frame, filedialog
import os


class First_Page_Frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        lable = Label(self, text = "This is main page")
        lable.pack(side="top", fill="x", pady=10)

        button = Button(self, text = "Create Project", command = lambda: controller.show_frame("Create_Project_Frame"))
        button.pack()

        button = Button(self, text = "Open Project", command = lambda: self.open_project())
        button.pack()
 
    # Allows to select which folder your data is in. 
    def open_project(self):
        directory = filedialog.askdirectory(initialdir=os.getcwd)
        if self.check_data_files(directory):
            data_error = Label(self, text = "The Data Is Compatable", fg="green", font=("Arial", 25))
        else:
            data_error = Label(self, text = "Error Data Not Compatable", fg="red", font=("Arial", 25))
        data_error.pack(side="bottom", fill="x", pady=10)
        data_error.after(5000, data_error.destroy)

    # Check if the directory selected has all necessary data to resume the project
    def check_data_files(self, directory):
        data_required = ["Config.json", "Node_info.json", "Packet_info.json"]
        for file in data_required:
            if file not in os.listdir(directory):
                return False
        return True

