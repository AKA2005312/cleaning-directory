import os
import shutil
import tkinter as tk
from tkinter import filedialog

def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    directory = filedialog.askdirectory()  # Open a dialog to select a directory
    return directory

def organize_files_by_extension(directory):
    if not directory:
        return

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = filename.split('.')[-1]
            extension_dir = os.path.join(directory, file_extension)

            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)

            shutil.move(os.path.join(directory, filename), os.path.join(extension_dir, filename))

if __name__ == "__main__":
    selected_directory = select_directory()
    organize_files_by_extension(selected_directory)
