
from tkinter import Label, Button, Tk, Frame


class First_Page_Frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        lable = Label(self, text = "This is main page")
        lable.pack(side="top", fill="x", pady=10)

        button = Button(self, text = "Create Project", command = lambda: controller.show_frame("Create_Project_Frame"))
        button.pack()

        button = Button(self, text = "Open Project")
        button.pack()
