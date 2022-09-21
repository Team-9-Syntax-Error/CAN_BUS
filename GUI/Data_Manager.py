import json
import os
import shutil
from tkinter import Label

"""
 Author: Mark-Anthony Avila
 
 By no means is this class representative of data management system. This is only temporary for the demo we are 
 creating. So far this class only communicates with Create_Project_Page to autofill GUI and grab user data
"""


# Temporary Data Management Class With JSON
class DataManager:
    # Holds JSON to Python Dictionary
    config_data = dict()

    # Test File Path
    config_file_path = "../User_Database/Default_Data_Config/Config.json"

    # Initializer
    def __init__(self):
        self.load_from_file()

    # Loads JSON Contents from CONFIG File
    def load_from_file(self):
        f = open(self.config_file_path)
        # Set Local JSON Dictionary
        self.config_data = json.load(f)
        f.close()

    # Receive User-Input From Project Configuration Page
    def receive_user_config_data(self, user_config_data):
        return self.dump_to_file(user_config_data)

    # Overwrite CONFIG File with Updated Information
    def dump_to_file(self, user_config_data):
        self.config_data = user_config_data
        
    
        folder_name = self.config_data['Project Configuration']['Project Title']

        if folder_name:

            # Making folder
            write_dir = "../User_Database/" + folder_name
            copy_dir = "/User_Database/" + folder_name
            os.mkdir(write_dir)
            os.chdir(write_dir)
            
            # Writing to folder
            f = open("Config.json", "w+")
            f.write(json.dumps(self.config_data, indent=1))
            f.close()
            print(os.getcwd())

            # Copy over Node_Info
            os.chdir("../")
            shutil.copy(os.getcwd() + "/Default_Data_Config/Node_info.json", os.getcwd()+"/"+folder_name)
            # Copy over Packet_Info
            shutil.copy(os.getcwd() + "/Default_Data_Config/Packet_info.json", os.getcwd()+"/"+folder_name)

        else:
            return False

    def get_config_data(self):
        self.load_from_file()
        return self.config_data
