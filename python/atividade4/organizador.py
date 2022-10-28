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
