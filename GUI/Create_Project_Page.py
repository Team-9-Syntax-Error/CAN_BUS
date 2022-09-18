import tkinter
from tkinter import Label, Button, Tk, Frame, Text, font


class Create_Project_Frame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.label_font = font.Font(family="Helvetica", size=15, weight="bold")
        self.text_font = font.Font(family="Helvetica", size=15)
        self.controller = controller
        self.place_labels()
        self.place_text()
        #teste
        button_first_page = Button(self, text = "First Page", command = lambda: controller.show_frame("First_Page_Frame"))
        button_first_page.pack()

    def place_labels(self):
        analist_initials = Label(self, text="Analyst Initials:", font=self.label_font)
        analist_initials.place(x=200, y=75)

        event_name = Label(self, text="Event Name:", font=self.label_font)
        event_name.place(x=200, y=125)

        event_date = Label(self, text="Event Date:", font=self.label_font)
        event_date.place(x=200, y=175)

        cc_id = Label(self, text="CAN Connector ID:", font=self.label_font)
        cc_id.place(x=200, y=225)

        v_id = Label(self, text="Vehicle ID:", font=self.label_font)
        v_id.place(x=200, y=275)

        baud_rate = Label(self, text="Baud Rate:", font=self.label_font)
        baud_rate.place(x=200, y=325)

        dbc_filename = Label(self, text="DBC File Name:", font=self.label_font)
        dbc_filename.place(x=200, y=375)

        bl_filename = Label(self, text="Blacklist File Name:", font=self.label_font)
        bl_filename.place(x=200, y=425)

    def place_text(self):
        analyst_initials_text = Text(self, height=1, width=15, font=self.text_font)
        analyst_initials_text.place(x=400, y=75)

        event_name_text = Text(self, height=1, width=15, font=self.text_font)
        event_name_text.place(x=400, y=125)

        event_date_text = Text(self, height=1, width=15, font=self.text_font)
        event_date_text.place(x=400, y=175)

        cc_id_text = Text(self, height=1, width=15, font=self.text_font)
        cc_id_text.place(x=400, y=225)

        v_id_text = Text(self, height=1, width=15, font=self.text_font)
        v_id_text.place(x=400, y=275)

        baud_rate_text = Text(self, height=1, width=15, font=self.text_font)
        baud_rate_text.place(x=400, y=325)

        dbc_filename_text = Text(self, height=1, width=15, font=self.text_font)
        dbc_filename_text.place(x=400, y=375)

        bl_filename_text = Text(self, height=1, width=15, font=self.text_font)
        bl_filename_text.place(x=400, y=425)

