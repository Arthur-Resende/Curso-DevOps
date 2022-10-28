import os
from unicodedata import name

def define_tipo_arquivo():
    arquivos = []
    pastas = []
    arquivos_downloads = os.scandir("/home/arthur/Downloads")
    for arquivo in arquivos_downloads:
        if arquivo.is_file() == True:
            arquivos.append(arquivo.name)
        elif arquivo.name != "pastas" and arquivo.name != "arquivos":
            pastas.append(arquivo.name)
    return {"arquivos": arquivos, "pastas": pastas}

def criar_pastas(arquivos_organizados: dict):
    if arquivos_organizados["pastas"] != []:
        try:
            os.mkdir("/home/arthur/Downloads/pastas")
        except:
            print("pasta já existe")

    if arquivos_organizados["arquivos"] != []:
        try:
            os.mkdir("/home/arthur/Downloads/arquivos")
        except:
            print("pasta já existe")

def mover_arquivos(caminho_base):
    for i in arquivos_por_tipo["arquivos"]:
        os.rename(caminho_base + i, caminho_base + "arquivos/" + i)

    for i in arquivos_por_tipo["pastas"]:
        os.rename(caminho_base + i, caminho_base + "pastas/" + i)

arquivos_por_tipo = define_tipo_arquivo()
criar_pastas(arquivos_por_tipo)
mover_arquivos("/home/arthur/Downloads/")