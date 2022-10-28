import os

file_types = {
    "Text Files":['.DOC', '.DOCX', '.EML', '.LOG', '.MSG', '.ODT', '.PAGES', '.RTF', '.TEX', '.TXT', '.WPD'],
    "Data Files":['.SDF', '.TAR', '.VCF', '.XML'],
    "Audio Files":['.AIF', '.FLAC', '.M3U', '.M4A', '.MID', '.MP3', '.OGG', '.WAV', '.WMA'],
    "Video Files":['.SWF', '.TS', '.VOB', '.WMV'],
    "3D Image Files":['.3DM', '.3DS', '.BLEND', '.DAE', '.FBX', '.MAX', '.OBJ'],
    "Raster Image Files":['.PNG', '.PSD', '.TGA', '.TIF'],
    "Vector Image Files":['.AI', '.CDR', '.EMF', '.EPS', '.PS', '.SKETCH', '.SVG', '.VSDX'],
    "Page Layout Files":['.AFPUB', '.INDD', '.OXPS', '.PDF', '.PMD', '.PUB', '.QXP', '.XPS'],
    "Spreadsheet Files":['.NUMBERS', '.ODS', '.XLR', '.XLS', '.XLSX'],
    "Database Files":['.PDB', '.SQL', '.SQLITE'],
    "Executable Files":['.JAR', '.RUN', '.SH'],
    "Game Files":['.BIN', '.DEM', '.GAM', '.GBA', '.NES', '.PAK', '.PKG', '.ROM', '.SAV', '.SAV'],
    "CAD Files":['.DGN', '.DWG', '.DXF', '.STEP', '.STL', '.STP'],
    "GIS Files":['.GPX', '.KML', '.KMZ', '.OSM'],
    "Web Files":['.CSR', '.CSS', '.HTML', '.JS', '.JSON', '.JSP', '.PHP', '.XHTML'],
    "Plugin Files":['.CRX', '.ECF', '.PLUGIN', '.SAFARIEXTZ', '.XPI'],
    "Font Files":['.FNT', '.OTF', '.TTF', '.WOFF', '.WOFF2'],
    "System Files":['.DLL', '.DMP', '.DRV', '.ICNS', '.ICO', '.LNK', '.REG', '.SYS'],
    "Settings Files":['.CFG', '.INI', '.PKG', '.PRF', '.SET'],
    "Encoded Files":['.ASC', '.BIN', '.ENC', '.MIM', '.UUE'],
    "Compressed Files":['.PKG', '.RAR', '.RPM', '.gz">.TAR.GZ', '.XAPK', '.ZIP', '.ZIPX'],
    "Disk Image Files":['.BIN', '.DMG', '.IMG', '.ISO', '.MDF', '.ROM', '.VCD', '.VMDK'],
    "Developer Files":['.KT', '.LUA', '.M', '.MD', '.PL', '.PY', '.SB3', '.SLN', '.SWIFT', '.UNITY', '.VB', '.VCXPROJ', '.XCODEPROJ', '.YML'],
    "Backup Files":['.ABK', '.ARC', '.BAK', '.TMP'],
    "Misc Files":['.CRDOWNLOAD', '.ICS', '.MSI', '.NOMEDIA', '.PART', '.PKPASS', '.TORRENT']
}

def define_file_types():
    download_files = os.scandir("/home/arthur/Downloads")
    file_by_type = []
    for file in download_files:
        file_ext = file.name[file.name.find('.'):].upper()
        if file.is_dir() == False:
            for i in file_types.keys():
                if file_ext in file_types[i]:
                    file_by_type.append(i)
        else:
            file_by_type.append("Folders")

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

# arquivos_por_tipo = define_file_types()
# create_dirs(arquivos_por_tipo)
# move_files("/home/arthur/Downloads/", arquivos_por_tipo)
define_file_types()