

from tkinter import Label, Button, Tk, Frame, Text


class Create_Project_Frame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        analist_initials = Label(self, text = "Analist Initials")
        analist_initials.place(x=150, y=75)

        analist_intials_text = Text(self, height = 1, width = 15)
        analist_intials_text.place(x=250, y=75)