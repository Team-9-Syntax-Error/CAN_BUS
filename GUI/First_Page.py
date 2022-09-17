
from tkinter import LEFT, TOP, Label, Button, Tk, Frame, filedialog, PhotoImage
import os


class First_Page_Frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        #Image for button
        self.open_project_img = PhotoImage(file = "D:\\Users\\Unity Projects\\CAN_BUS\\GUI\\OpenProject.png")
        self.create_project_img = PhotoImage(file = "D:\\Users\\Unity Projects\\CAN_BUS\\GUI\\CreateProject.png")

        #Define background image
        self.background = PhotoImage(file = "D:\\Users\\Unity Projects\\CAN_BUS\\GUI\\Background.png")
        
        #Show Image
        background_label = Label(self, image = self.background)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        lable = Label(self, text = "This is main page", bg="#00528C", font="Helvetica, 32")
        lable.pack(side="top", fill="x", pady=10)

        button = Button(self, text = "Create Project", image=self.create_project_img, compound=TOP, command = lambda: controller.show_frame("Create_Project_Frame"), font="Helvetica, 25")
        button.place(relx=0.1, rely=0.4)

        button = Button(self, text = "Open Project", image=self.open_project_img, compound=TOP, command = lambda: self.open_project(), font="Helvetica, 25")
        button.place(relx=0.6, rely=0.4)
 
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

