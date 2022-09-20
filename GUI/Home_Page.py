
from re import fullmatch
from tkinter import LEFT, TOP, Label, Button, Tk, Frame, filedialog, PhotoImage
import os


class Home_Page_Frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        lable = Label(self, text = "This is Home Page", bg="#00528C", font="Helvetica, 32")
        lable.pack(side="top", fill="x", pady=10)

        

