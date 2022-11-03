import errno
import os
# from file_types import file_types as file_type_list

file_type_list = {
    "Video files": ['.MPG', '.MOV', '.WMV', '.RM'],
    "Text Files":['.DOC', '.DOCX', '.EML', '.LOG', '.MSG', '.ODT', '.PAGES', '.RTF', '.TEX', '.TXT', '.WPD'],
    "Data Files":['.SDF', '.TAR', '.VCF', '.XML'],
    "Audio Files":['.AIF', '.FLAC', '.M3U', '.M4A', '.MID', '.MP3', '.OGG', '.WAV', '.WMA'],
    "Video Files":['.SWF', '.TS', '.VOB', '.WMV'],
    "3D Image Files":['.3DM', '.3DS', '.BLEND', '.DAE', '.FBX', '.MAX', '.OBJ'],
    "Raster Image Files":['.PNG', '.PSD', '.TGA', '.TIF', '.JPG'],
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
    "Misc Files":['.CRDOWNLOAD', '.ICS', '.MSI', '.NOMEDIA', '.PART', '.PKPASS', '.TORRENT'],
}

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
        for file in os.scandir(self.path):
            extention_index = file.name.find('.')
            extention = file.name[extention_index:].upper()
            if file.is_dir() == False:
                for folder in file_type_list:
                    extention_list = file_type_list[folder]
                    if extention in extention_list:
                        if folder not in self.organized_files:
                            self.organized_files[folder] = [file.name]
                        else:
                            self.organized_files[folder].append(file.name)

                if "Others" not in self.organized_files:
                    self.organized_files["Others"] = [file.name]
                else:
                    self.organized_files["Others"].append(file.name)

            elif (file.name != "Folders" ) and (file.name != "Others") and file.name not in file_type_list.keys():
                self.organized_files["Folders"] = file.name
        print(self.organized_files)

    def create_dirs(self):
        for folder in self.organized_files.keys():
            try:
                os.mkdir("%s/%s" %(self.path, folder))
            except OSError as e:
                if e.errno == 17:
                    pass
                else:
                    raise e


    def move_files(self):
        for folder in self.organized_files.keys():
            for file in self.organized_files[folder]:
                try:
                    src = "/%s/%s" %(self.path, file)
                    dst = "/%s/%s/%s" %(self.path, folder, file)
                    os.rename(src, dst)
                except Exception as e:
                    raise e

organizador = Organizer()
organizador.define_file_types()
organizador.create_dirs()
organizador.move_files()