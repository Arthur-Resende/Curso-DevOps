import os

def define_tipo_arquivo():
    arquivos = []
    pastas = []
    arquivos_downloads = os.scandir("/home/arthur/Downloads")
    for arquivo in arquivos_downloads:
        if arquivo.is_file() == True:
            arquivos.append(arquivo.name)
        else:
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

arquivos_por_tipo = define_tipo_arquivo()
criar_pastas(arquivos_por_tipo)