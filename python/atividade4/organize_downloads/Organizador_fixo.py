import os
from file_types import file_types as file_type_list

class Organizer():
    def __init__(self):
        self.user = os.getlogin()
        self.current_os = os.name
        if self.current_os == "posix":
            self.path = "/home/%s/Downloads" %self.user
        else:
            self.path = "C:/Users/%s/Downloads" %self.user

        self.organized_files = {}

    def define_file_types(self):
        folder_files = os.scandir(self.path)
        for downloaded_file in folder_files:
            extention_index = downloaded_file.name.find('.')
            file_extention = downloaded_file.name[extention_index:].upper()
            if downloaded_file.is_dir() == False:
                for file_type in file_type_list:
                    extention_list = file_type_list[file_type]
                    if file_extention in extention_list:
                        self.organized_files[downloaded_file.name] = file_type

            elif downloaded_file.name not in file_type_list.keys():
                self.organized_files[downloaded_file.name] = "Folders"

    def create_dirs(self):
        for file_type in self.organized_files.values():
            try:
                os.mkdir("%s/%s" %(self.path, file_type))
            except:
                pass

    def move_files(self):
        for file in self.organized_files.keys():
            try:
                src = "/%s/%s" %self.path, file
                dst = "/%s/%s/%s" %(self.path, self.organized_files[file], file)
                os.rename(src, dst)
            except:
                pass