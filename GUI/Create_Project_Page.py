import tkinter
from tkinter import Label, Button, Tk, Frame, Text, font, PhotoImage, Canvas
from Data_Manager import DataManager


class Create_Project_Frame(Frame):
    # Initialize Text
    proj_title_text = Text
    analyst_initials_text = Text
    event_name_text = Text
    event_date_text = Text
    cc_id_text = Text
    v_id_text = Text
    baud_rate_text = Text
    dbc_filename_text = Text
    bl_filename_text = Text

    def __init__(self, parent, controller):
        # Get CONFIG Data
        self.data_manager = DataManager()
        self.config_data = self.data_manager.get_config_data()
        self.proj_data = self.config_data['Project Configuration']
        self.bg_img = PhotoImage(file="Images/Background.png")
        self.pr = parent
        self.label_pos_mult = 35

        Frame.__init__(self, parent)
        self.label_font = font.Font(family="Helvetica", size=15, weight="bold")
        self.text_font = font.Font(family="Helvetica", size=15)
        self.title_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.button_font = font.Font(weight="bold", size=11)
        self.controller = controller
        self.place_labels()
        self.place_text()
        self.place_buttons()

    def retrieve_data(self):
        self.config_data['Project Configuration'].update({'Project Title': self.proj_title_text.get("1.0", 'end-1c')})
        self.config_data['Project Configuration'].update({'Analyst Initials': self.analyst_initials_text.get("1.0", 'end-1c')})
        self.config_data['Project Configuration'].update({'Event Name': self.event_name_text.get("1.0", 'end-1c')})
        self.config_data['Project Configuration'].update({'Event Date': self.event_date_text.get("1.0", 'end-1c')})
        self.config_data['Project Configuration'].update({'Can Connector ID': self.cc_id_text.get("1.0", 'end-1c')})
        self.config_data['Project Configuration'].update({'Vehicle ID': self.v_id_text.get("1.0", 'end-1c')})
        self.config_data['Project Configuration'].update({'Baud Rate': self.baud_rate_text.get("1.0", 'end-1c')})
        self.config_data['Project Configuration'].update({'DBC File Name': self.dbc_filename_text.get("1.0", 'end-1c')})
        self.config_data['Project Configuration'].update({'Black List File Name': self.bl_filename_text.get("1.0", 'end-1c')})
        # Send User-Input to Data Manager
        self.data_manager.receive_user_config_data(self.config_data)

    def place_buttons(self):
        back_button = Button(self, text="Back", activebackground="light blue", font=self.button_font, command=lambda: self.controller.show_frame("First_Page_Frame"))
        back_button.pack()
        back_button.place(x=10, y=10)

        save_project_button = Button(self, text="Create Project", activebackground="light blue", font=self.button_font, command=lambda: self.retrieve_data())
        save_project_button.pack()
        save_project_button.place(x=625, y=460)

    def place_labels(self):
        background_label = Label(self, image=self.bg_img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self, text="Project Configuration", font=self.title_font)
        title.place(x=230, y=10)

        proj_title_label = Label(self, text="Project Title:", font=self.label_font)
        proj_title_label.place(x=200, y=25+self.label_pos_mult)

        analist_initials = Label(self, text="Analyst Initials:", font=self.label_font)
        analist_initials.place(x=200, y=75+self.label_pos_mult)

        event_name = Label(self, text="Event Name:", font=self.label_font)
        event_name.place(x=200, y=125+self.label_pos_mult)

        event_date = Label(self, text="Event Date:", font=self.label_font)
        event_date.place(x=200, y=175+self.label_pos_mult)

        cc_id = Label(self, text="CAN Connector ID:", font=self.label_font)
        cc_id.place(x=200, y=225+self.label_pos_mult)

        v_id = Label(self, text="Vehicle ID:", font=self.label_font)
        v_id.place(x=200, y=275+self.label_pos_mult)

        baud_rate = Label(self, text="Baud Rate:", font=self.label_font)
        baud_rate.place(x=200, y=325+self.label_pos_mult)

        dbc_filename = Label(self, text="DBC File Name:", font=self.label_font)
        dbc_filename.place(x=200, y=375+self.label_pos_mult)

        bl_filename = Label(self, text="Blacklist File Name:", font=self.label_font)
        bl_filename.place(x=200, y=425+self.label_pos_mult)

    def place_text(self):
        self.proj_title_text = Text(self, height=1, width=15, font=self.text_font)
        self.proj_title_text.place(x=400, y=25+self.label_pos_mult)

        self.analyst_initials_text = Text(self, height=1, width=15, font=self.text_font)
        self.analyst_initials_text.place(x=400, y=75+self.label_pos_mult)
        self.analyst_initials_text.insert('1.0', self.proj_data.get('Analyst Initials'))

        self.event_name_text = Text(self, height=1, width=15, font=self.text_font)
        self.event_name_text.place(x=400, y=125+self.label_pos_mult)

        self.event_date_text = Text(self, height=1, width=15, font=self.text_font)
        self.event_date_text.place(x=400, y=175+self.label_pos_mult)

        self.cc_id_text = Text(self, height=1, width=15, font=self.text_font)
        self.cc_id_text.place(x=400, y=225+self.label_pos_mult)

        self.v_id_text = Text(self, height=1, width=15, font=self.text_font)
        self.v_id_text.place(x=400, y=275+self.label_pos_mult)

        self.baud_rate_text = Text(self, height=1, width=15, font=self.text_font)
        self.baud_rate_text.place(x=400, y=325+self.label_pos_mult)

        self.dbc_filename_text = Text(self, height=1, width=15, font=self.text_font)
        self.dbc_filename_text.place(x=400, y=375+self.label_pos_mult)

        self.bl_filename_text = Text(self, height=1, width=15, font=self.text_font)
        self.bl_filename_text.place(x=400, y=425+self.label_pos_mult)
