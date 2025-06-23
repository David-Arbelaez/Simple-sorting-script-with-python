import os
import sys
import logging
from time import sleep
from shutil import move
from os import scandir, rename
from watchdog.observers import Observer
from os.path import exists, splitext, join
from watchdog.events import FileSystemEventHandler


# Destination folder to keep track (path)
source_dir = r"D:\JDownloads"

# Folders to set up files (customizable)
dest_dir_notes = r"D:\JDownloads\TXT"
dest_dir_images = r"D:\JDownloads\Images"
dest_dir_scripts = r"D:\JDownloads\Scripts"
dest_dir_documents = r"D:\JDownloads\Documents"


# Supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

# Supported document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

# Supported note types
note_extensions = [".txt"]

# Supported script types
script_extensions = [".py"]


# If file exists, adds a number tothe end of the filename
def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name

# Move the file
def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

# This function will run whenever there is a change in the source dir
class MoverHandler(FileSystemEventHandler):
    
    
    def on_modified(self, event):
        sleep(3)
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_note_files(entry, name)
                self.check_image_files(entry, name)
                self.check_script_files(entry, name)
                self.check_document_files(entry, name)
                

    # .upper is for not missing out on files with uppercase extensions
    def check_note_files(self, entry, name): 
        for note_extension in note_extensions:
            if name.endswith(note_extension) or name.endswith(note_extension.upper()):
                move_file(dest_dir_notes, entry, name)
                logging.info(f"Moved note file: {name}")

    def check_image_files(self, entry, name): 
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_images, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):  
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")

    def check_script_files(self, entry, name):  
        for scripts_extension in script_extensions:
            if name.endswith(scripts_extension) or name.endswith(scripts_extension.upper()):
                move_file(dest_dir_scripts, entry, name)
                logging.info(f"Moved script file: {name}")



# Initialization code
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()








