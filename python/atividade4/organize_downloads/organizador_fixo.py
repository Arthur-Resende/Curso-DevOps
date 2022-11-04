"""
Organizes files in download folder
"""
import os

file_type_list = {
    "Video files": [".MPG", ".MOV", ".WMV", ".RM"],
    "Text Files":[".DOC", ".DOCX", ".EML", ".LOG",".MSG", ".ODT", ".PAGES", ".RTF", ".TEX", ".TXT",".WPD"],
    "Data Files":[".SDF", ".TAR", ".VCF", ".XML"],
    "Audio Files":[".AIF", ".FLAC", ".M3U", ".M4A", ".MID", ".MP3", ".OGG", ".WAV", ".WMA"],
    "Video Files":[".SWF", ".TS", ".VOB", ".WMV"],
    "Raster Image Files":[".PNG", ".PSD", ".TGA", ".TIF", ".JPG"],
    "Vector Image Files":[".AI", ".CDR", ".EMF", ".EPS", ".PS", ".SKETCH", ".SVG", ".VSDX"],
    "Page Layout Files":[".AFPUB", ".INDD", ".OXPS", ".PDF", ".PMD", ".PUB", ".QXP", ".XPS"],
    "Spreadsheet Files":[".NUMBERS", ".ODS", ".XLR", ".XLS", ".XLSX"],
    "Executable Files":[".JAR", ".RUN", ".SH"],
    "Game Files":[".BIN", ".DEM", ".GAM", ".GBA", ".NES", ".PAK", ".PKG", ".ROM", ".SAV", ".SAV"],
    "Web Files":[".CSR", ".CSS", ".HTML", ".JS", ".JSON", ".JSP", ".PHP", ".XHTML"],
    "Font Files":[".FNT", ".OTF", ".TTF", ".WOFF", ".WOFF2"],
    "System Files":[".DLL", ".DMP", ".DRV", ".ICNS", ".ICO", ".LNK", ".REG", ".SYS"],
    "Settings Files":[".CFG", ".INI", ".PKG", ".PRF", ".SET"],
    "Encoded Files":[".ASC", ".BIN", ".ENC", ".MIM", ".UUE"],
    "Compressed Files":[".PKG", ".RAR", ".RPM", ".gz", ".TAR.GZ", ".XAPK", ".ZIP", ".ZIPX"],
    "Disk Image Files":[".BIN", ".DMG", ".IMG", ".ISO", ".MDF", ".ROM", ".VCD", ".VMDK"],
    "Developer Files":[".KT", ".LUA", ".M", ".MD", ".PL", ".PY", ".SB3", ".SLN", ".SWIFT", ".UNITY", ".VB",".VCXPROJ", ".XCODEPROJ", ".YML"],
    "Backup Files":[".ABK", ".ARC", ".BAK", ".TMP"],
    "Misc Files":[".CRDOWNLOAD", ".ICS", ".MSI", ".NOMEDIA", ".PART", ".PKPASS", ".TORRENT"],
}

def append_dict(key, dictionary, value):
    """
    Checks if key exists in dictionary, if it exists value
    is appended, otherwise key is created and value is
    assigned to key as a list.

    Assumes values from existing key are a list, therefore
    does not check before attempting to append.
    """
    if key not in dictionary:
        dictionary[key] = [value]
    else:
        dictionary[key].append(value)

class Organizer():
    """
    Class of download folder oganizer, has 3 functions
    - define_file_types(): assigns files to foldes
    - create_dirs(): creates assigned directiories for files
      to go to.
    - move_files(): moves files towards assigned directory.
    """
    def __init__(self):
        self.user = os.getlogin()
        self.current_os = os.name
        if self.current_os == "posix":
            self.path = f"/home/{self.user}/Downloads"
        else:
            self.path = f"C:/Users/{self.user}/Downloads"

        self.organized_files = {}

    def define_file_types(self):
        """
        Scans Downloads dir, checks name of all files,
        and assigns files to folders based on the extention
        of the file.

        Files and assigned folders saved in dictionary with
        format:
            organized_files {
                "<folder_1>": [<file list>],
                "<folder_2>": [<file list>],
                ...
                "<folder_n>": [<file list>]
            }
        """
        for file in os.scandir(self.path):
            if file.is_dir() is False:
                item_is_defined = False
                for folder_file in file_type_list.items():
                    extention = file.name[file.name.find('.'):].upper()
                    if extention in folder_file[1]:
                        append_dict(folder_file[0], self.organized_files, file.name)
                        item_is_defined = True

                if item_is_defined is False:
                    append_dict("Others", self.organized_files, file.name)

            elif (
                file.name != "Folders" and
                file.name != "Others" and
                file.name not in file_type_list
                ):
                append_dict("Folders", self.organized_files, file.name)

    def create_dirs(self):
        """
        Reads folder-file dictionary and creates all assigned
        folders.
        """
        for folder in self.organized_files:
            try:
                os.mkdir(f"{self.path}/{folder}")
            except OSError as error:
                if error.errno == 17:
                    pass
                else:
                    raise error

    def move_files(self):
        """
        Reads folder-file dictionary and moves files from
        Downloads dir to assiged folder.
        """
        for folder_file in self.organized_files.items():
            for file in folder_file[1]:
                try:
                    src = f"/{self.path}/{file}"
                    dst = f"/{self.path}/{folder_file[0]}/{file}"
                    os.rename(src, dst)
                except Exception as error:
                    raise error
