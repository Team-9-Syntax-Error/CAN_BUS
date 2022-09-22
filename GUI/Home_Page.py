
from re import fullmatch
from tkinter import BOTH, CENTER, LEFT, TOP, Canvas, Label, Button, Menu, Tk, Frame, filedialog, PhotoImage, ttk
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
        
        #current_project_directory, current_project_title = self.current_project_directory()
        lable = Label(self, text = "Home Page", bg="gray", font="Helvetica, 32")
        lable.pack(side="top", fill="x", pady=10)
        
        lable = Label(self, text = "Traffic", bg="white", font="Helvetica, 16")
        lable.pack(side="top", fill="x", pady=10)

        tree = ttk.Treeview(self, column=("Id", "Time", "Data"), show='headings', height=2)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="ID")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="TIME")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="DATE")

        #tree.column("Id",width= 200) #Not necesari at the moment
        tree.pack()

        lable = Label(self, text = "CAN Map", bg="white", font="Helvetica, 16")
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
        submenu2 = Menu(menu1)
        submenu3 = Menu(menu1)
        submenu4 = Menu(menu1)
        submenu5 = Menu(menu1)
      
        menu1.add_cascade(label = "File", menu = submenu1)
        submenu1.add_command(label = "New", command = "Modificar//")
        submenu1.add_command(label = "Open", command = "Modificar//")
        submenu1.add_command(label = "Save", command = "Modificar//")

        menu1.add_cascade(label = "View", menu = submenu2)
        submenu2.add_command(label = "Zoom-In", command = "Modificar//")
        submenu2.add_command(label = "Zoom-Out", command = "Modificar//")

        menu1.add_cascade(label = "Packet", menu = submenu3)
        submenu3.add_command(label = "Show", command = "Modificar//")
        
        menu1.add_cascade(label = "Edit", menu = submenu4)
        submenu4.add_command(label = "Add", command = "Modificar//")
        submenu4.add_command(label = "Remove", command = "Modificar//")
        submenu4.add_command(label = "Connect", command = "Modificar//")
        
        menu1.add_cascade(label = "Nodes", menu = submenu5)
        submenu5.add_command(label = "Show", command = "Modificar//")
        submenu5.add_command(label = "Hide", command = "Modificar//")
        submenu5.add_command(label = "Highlight", command = "Modificar//")
        
    def current_project_directory(self):
        with open("../User_Database/Current_Project.json", 'r') as openfile:
             json_object = json.load(openfile)
             current_project_directory = json_object["Current_Project"]
             current_project_title = json_object["Project_Title"]
        return current_project_directory, current_project_title
        

