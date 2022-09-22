<<<<<<< HEAD
import tkinter
=======
>>>>>>> 42427b652f1d167441bee1549aa35ad0eb6dfb68
from tkinter import BOTH, Label, Button, Tk, Frame, Text, font, PhotoImage, Canvas
from Data_Manager import DataManager


class Create_Project_Frame(Frame):
    # User-Input Data Dictionary
    local_user_data = {"Project Configuration": {}}
    local_user_config_data = local_user_data['Project Configuration']

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
        self.controller = controller
        self.data_manager = DataManager()
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
        # Retrieve Text Input and Store in local CONFIG Data Dictionary
        self.local_user_config_data.update({'Project Title': self.proj_title_text.get("1.0", 'end-1c')})
        self.local_user_config_data.update({'Analyst Initials': self.analyst_initials_text.get("1.0", 'end-1c')})
        self.local_user_config_data.update({'Event Name': self.event_name_text.get("1.0", 'end-1c')})
        self.local_user_config_data.update({'Event Date': self.event_date_text.get("1.0", 'end-1c')})
        self.local_user_config_data.update({'Can Connector ID': self.cc_id_text.get("1.0", 'end-1c')})
        self.local_user_config_data.update({'Vehicle ID': self.v_id_text.get("1.0", 'end-1c')})
        self.local_user_config_data.update({'Baud Rate': self.baud_rate_text.get("1.0", 'end-1c')})
        self.local_user_config_data.update({'DBC File Name': self.dbc_filename_text.get("1.0", 'end-1c')})
        self.local_user_config_data.update({'Black List File Name': self.bl_filename_text.get("1.0", 'end-1c')})

        # Send User-Input to Data Manager
        if self.data_manager.dump_data("Project Configuration", self.local_user_config_data) == False:
            data_error = Label(self, text = "Error Project Title Missing", fg="red", font=("Arial", 25))
            data_error.pack(side="bottom", fill="x", pady=10)
            data_error.after(5000, data_error.destroy)
        else:
            self.controller.show_frame("Home_Page_Frame")

    def place_buttons(self):
        back_button = Button(self, text="Back", activebackground="light blue", font=self.button_font, command=lambda: self.controller.show_frame("First_Page_Frame"))
        back_button.pack()
        back_button.place(x=10, y=10)

        save_project_button = Button(self, text="Create Project", activebackground="light blue", font=self.button_font, command=lambda: self.retrieve_data(), )
        save_project_button.pack()
        save_project_button.place(x=625, y=460)

    def place_labels(self):
        backgroundInformation = Canvas(self, width=100, height=100)
        backgroundInformation.create_image(0, 0, image=self.bg_img, anchor="nw")

        backgroundInformation.create_text(400, 20, text="Project Configuration", font=self.title_font, fill="white")
        backgroundInformation.pack(expand=True, fill=BOTH)
        
        backgroundInformation.create_text(292, 72, text="Project Title:", font=self.title_font, fill="white")
        backgroundInformation.pack(expand=True, fill=BOTH)
        
        backgroundInformation.create_text(275, 122, text="Analyst Initials:", font=self.title_font, fill="white")
        backgroundInformation.pack(expand=True, fill=BOTH)
        
        backgroundInformation.create_text(291, 172, text="Event Name:", font=self.title_font, fill="white")
        backgroundInformation.pack(expand=True, fill=BOTH)

        backgroundInformation.create_text(298, 225, text="Event Date:", font=self.title_font, fill="white")
        backgroundInformation.pack(expand=True, fill=BOTH)

        backgroundInformation.create_text(247, 274, text="CAN Connector ID:", font=self.title_font, fill="white")
        backgroundInformation.pack(expand=True, fill=BOTH)

        backgroundInformation.create_text(304, 324, text="Vehicle ID:", font=self.title_font, fill="white")
        backgroundInformation.pack(expand=True, fill=BOTH)

        backgroundInformation.create_text(304, 374, text="Baud Rate:", font=self.title_font, fill="white")
        backgroundInformation.pack(expand=True, fill=BOTH)

        backgroundInformation.create_text(278, 424, text="DBC File Name:", font=self.title_font, fill="white")
        backgroundInformation.pack(expand=True, fill=BOTH)

        backgroundInformation.create_text(248, 474, text="Blacklist File Name:", font=self.title_font, fill="white")
        backgroundInformation.pack(expand=True, fill=BOTH)

    def place_text(self):
        self.proj_title_text = Text(self, height=1, width=15, font=self.text_font)
        self.proj_title_text.place(x=400, y=25+self.label_pos_mult)

        self.analyst_initials_text = Text(self, height=1, width=15, font=self.text_font)
        self.analyst_initials_text.place(x=400, y=75+self.label_pos_mult)
        self.analyst_initials_text.insert('1.0', self.data_manager.get('Analyst Initials'))

        self.event_name_text = Text(self, height=1, width=15, font=self.text_font)
        self.event_name_text.place(x=400, y=125+self.label_pos_mult)
        self.event_name_text.insert('1.0', self.data_manager.get('Event Name'))

        self.event_date_text = Text(self, height=1, width=15, font=self.text_font)
        self.event_date_text.place(x=400, y=175+self.label_pos_mult)
        self.event_date_text.insert('1.0', self.data_manager.get('Event Date'))

        self.cc_id_text = Text(self, height=1, width=15, font=self.text_font)
        self.cc_id_text.place(x=400, y=225+self.label_pos_mult)
        self.cc_id_text.insert('1.0', self.data_manager.get('Can Connector ID'))

        self.v_id_text = Text(self, height=1, width=15, font=self.text_font)
        self.v_id_text.place(x=400, y=275+self.label_pos_mult)
        self.v_id_text.insert('1.0', self.data_manager.get('Vehicle ID'))

        self.baud_rate_text = Text(self, height=1, width=15, font=self.text_font)
        self.baud_rate_text.place(x=400, y=325+self.label_pos_mult)
        self.baud_rate_text.insert('1.0', self.data_manager.get('Baud Rate'))

        self.dbc_filename_text = Text(self, height=1, width=15, font=self.text_font)
        self.dbc_filename_text.place(x=400, y=375+self.label_pos_mult)
        self.dbc_filename_text.insert('1.0', self.data_manager.get('DBC File Name'))

        self.bl_filename_text = Text(self, height=1, width=15, font=self.text_font)
        self.bl_filename_text.place(x=400, y=425+self.label_pos_mult)
        self.bl_filename_text.insert('1.0', self.data_manager.get('Black List File Name'))
