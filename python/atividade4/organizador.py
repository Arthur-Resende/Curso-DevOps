import os
import file_types as file_type_dict

def define_file_types():
    download_file_list = os.scandir("/home/arthur/Downloads")
    files_by_type = {}
    for downloaded_file in download_file_list:
        file_extention = downloaded_file.name[downloaded_file.name.find('.'):].upper()
        if downloaded_file.is_dir() == False:
            for file_type in file_type_dict.keys():
                file_type_list = file_type_dict[file_type]
                if file_extention in file_type_list:
                    files_by_type[downloaded_file.name] = file_type

        elif downloaded_file.name not in file_type_dict.keys():
            files_by_type[downloaded_file.name] = "Folders"

    return files_by_type

def create_dirs(files_by_type: dict):
    for file_type in files_by_type.items():
        try:
            os.mkdir("/home/arthur/Downloads/%s" %file_type)
        except:
            pass

def move_files(base_path, files_by_type: dict):
    for file in files_by_type.keys():
        src = "%s/%s" %(base_path, file)
        dst = "%s/%s/%s" %(base_path, files_by_type[file], file)
        os.rename(src, dst)

arquivos_por_tipo = define_file_types()
create_dirs(arquivos_por_tipo)
move_files("/home/arthur/Downloads", arquivos_por_tipo)