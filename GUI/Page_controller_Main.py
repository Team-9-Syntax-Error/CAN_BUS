

from msilib.schema import Directory
from tkinter import Tk, Frame
from Create_Project_Page import Create_Project_Frame
from First_Page import First_Page_Frame
from Home_Page import Home_Page_Frame

class CAN_BUS_GUI(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        self.winfo_toplevel().title("CAN BUS")
        container = Frame(self)
        container.pack(side = "top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # All pages get stored in this dictionary
        self.frames ={}

        # Loading all pages for the GUI
        for F in (First_Page_Frame, Create_Project_Frame, Home_Page_Frame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0,column=0, sticky="nsew")

        # The GUI opens up with the first page 
        self.show_frame("First_Page_Frame")

    # This function is the controller to change the pages (Frames) 
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
    
# This starts everything
if __name__ == "__main__":
    can_gui = CAN_BUS_GUI()
    can_gui.geometry("750x500")
    can_gui.mainloop()