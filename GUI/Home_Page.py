
from re import fullmatch
from tkinter import BOTH, LEFT, TOP, Canvas, Label, Button, Menu, Tk, Frame, filedialog, PhotoImage
import os

#from matplotlib.font_manager import json_dump
from First_Page import First_Page_Frame
import json

#Path
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)
full_path = path + "/Images/"
canCar_path = full_path + "CAN Car.png"


class Home_Page_Frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        
        current_project_directory, current_project_title = self.current_project_directory()
        lable = Label(self, text = current_project_title, bg="#00528C", font="Helvetica, 32")
        lable.pack(side="top", fill="x", pady=10)

      #
        self.carImage = PhotoImage(file = canCar_path)
      
      #This handles the CAN bus image
        canBus = Canvas(self, width=20, height=20)
        canBus.create_image(500, 100, image = self.carImage) #Handle Image
        canBus.pack(expand=True, fill=BOTH)

        #Menu
        menu1 = Menu(controller)
        controller.config(menu = menu1)

        submenu1 = Menu(menu1)
        menu1.add_cascade(label = "File", menu = submenu1)
        submenu1.add_command(label = "Save", command = "Modificar//")

        menu1.add_cascade(label = "View", menu = submenu1)
        submenu1.add_command(label = "Somethin", command = "Modificar//")

        menu1.add_cascade(label = "Packet", menu = submenu1)
        submenu1.add_command(label = "Show", command = "Modificar//")

        
    def current_project_directory(self):
        with open("../User_Database/Current_Project.json", 'r') as openfile:
             json_object = json.load(openfile)
             current_project_directory = json_object["Current_Project"]
             current_project_title = json_object["Project_Title"]
        return current_project_directory, current_project_title
        

