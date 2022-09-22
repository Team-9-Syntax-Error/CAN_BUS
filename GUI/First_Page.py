
from doctest import master
from email.mime import image
from logging import root
from re import fullmatch
from tkinter import BOTH, LEFT, N, TOP, Canvas, Label, Button, Tk, Frame, filedialog, PhotoImage
import os
import tkinter.font as tkFont
import json


class First_Page_Frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.open_project_directory = ""
        self.controller = controller

        #Path
        path = os.path.dirname(os.path.realpath(__file__))
        os.chdir(path)
        full_path = path + "/Images/"
        background_path = full_path + "Background.png"
        createImg_path = full_path + "CreateProject.png"
        openImg_path = full_path + "OpenProject.png"


        #Font variables
        titleFont = tkFont.Font(family="Courier", size=50, weight="bold")
        buttonFont = "Helvetica, 25"

        #Image for button
        self.open_project_img = PhotoImage(file = openImg_path)
        self.create_project_img = PhotoImage(file = createImg_path)

        #Image for background
        self.background = PhotoImage(file = background_path)
        
        #Handle background for Main Page
        #backgroundInformation handles the background image and the text
        backgroundInformation = Canvas(self, width=100, height=100)
        backgroundInformation.create_image(0, 0, image = self.background, anchor = "nw") #Handle Image
        backgroundInformation.create_text(385, 100, text='Main Page', font=titleFont, fill="white") #Handle Text
        backgroundInformation.pack(expand=True, fill=BOTH)

        #Buttons (Create & Open Project)
        #Handle the creation of buttons in the Main Page/First_page
        button = Button(self, text = "Create Project", image=self.create_project_img, compound=TOP, command = lambda: controller.show_frame("Create_Project_Frame"), font = buttonFont)
        button.place(relx=0.1, rely=0.4)

        button = Button(self, text = "Open Project", image=self.open_project_img, compound=TOP, command = lambda: self.open_project(backgroundInformation), font = buttonFont)
        button.place(relx=0.6, rely=0.4)
 
    #Allows to select which folder your data is in. 
    def open_project (self, backgroundInformation):
        os.chdir("../User_Database")
        print(os.getcwd())
        directory = filedialog.askdirectory(initialdir=os.getcwd())
        print(directory)
        print(os.getcwd())
        os.chdir("../GUI")
        #Font variable
        messageFont = tkFont.Font(family="Calibri", size=25, weight="bold")

        if directory:
            not_missing_files = self.check_data_files(directory)
            with open("../User_Database/Current_Project.json", 'r') as openfile:
                json_object = json.load(openfile)
                c_pt = json_object["Project_Title"]


            # If the directory reports true we check for files and make our "Current Project path avaliable"
            if not_missing_files is True:
                data_error = backgroundInformation.create_text(385, 450, text='The Data Is Compatable', font = messageFont, fill="green")
                with open("../User_Database/Current_Project.json", "w") as outfile:
                    json.dump({"Current_Project": directory,  "Project_Title": c_pt}, outfile)
                self.controller.show_frame("Home_Page_Frame")

            else:
                data_error = backgroundInformation.create_text(385, 450, text="Error: " + not_missing_files + " Not found", font = messageFont, fill="red")
            backgroundInformation.pack(expand=True, fill=BOTH)
            self.after(5000, lambda: backgroundInformation.delete(data_error)) #Removes message after 5000


    #Check if the directory selected has all necessary data to resume the project
    def check_data_files(self, directory):
        data_required = ["Config.json", "Node_info.json", "Packet_info.json"]
        for file in data_required:
            if file not in os.listdir(directory):
                return file
        return True
    
    