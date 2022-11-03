from organize_downloads.organizador_fixo import Organizer

organizer = Organizer()
organizer.define_file_types()
organizer.create_dirs()
organizer.move_files()
