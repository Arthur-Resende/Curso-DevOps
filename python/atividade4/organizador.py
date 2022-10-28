import os
from unicodedata import name

def define_file_types():
    file_by_type = {"files": [], "dirs": []}
    download_files = os.scandir("/home/arthur/Downloads")
    for file in download_files:
        if file.is_file() == True:
            file_by_type["files"].append(file.name)

        elif file.name != "pastas" and file.name != "arquivos":
            arquivos_por_tipo["dirs"].append(file.name)

    return file_by_type

def create_dirs(files_by_type: dict):
    if files_by_type["dirs"] != []:
        try:
            os.mkdir("/home/arthur/Downloads/pastas")
        except:
            pass

    if files_by_type["files"] != []:
        try:
            os.mkdir("/home/arthur/Downloads/arquivos")
        except:
            pass

def move_files(base_path, files_by_type: dict):
    for i in files_by_type["files"]:
        os.rename(base_path + i, base_path + "arquivos/" + i)

    for i in files_by_type["dirs"]:
        os.rename(base_path + i, base_path + "pastas/" + i)

arquivos_por_tipo = define_file_types()
create_dirs(arquivos_por_tipo)
move_files("/home/arthur/Downloads/", arquivos_por_tipo)