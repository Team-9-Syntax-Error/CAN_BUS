
from re import fullmatch
from tkinter import LEFT, TOP, Label, Button, Tk, Frame, filedialog, PhotoImage
import os
from First_Page import First_Page_Frame
import json


class Home_Page_Frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        with open("../User_Database/Current_Project.json", 'r') as openfile:
             json_object = json.load(openfile)

        current_project_directory = json_object["Current_Project"]
        lable = Label(self, text = current_project_directory, bg="#00528C", font="Helvetica, 32")
        lable.pack(side="top", fill="x", pady=10)



        

