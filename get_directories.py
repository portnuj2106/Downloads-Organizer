from tkinter import filedialog

import tkinter as tk


root = tk.Tk()
root.withdraw()


def get_directory():
    directory = filedialog.askdirectory(title="Select a directory to sort")
    if directory:
        convert_to_double_slash(directory)
    return convert_to_double_slash(directory)


def get_dest_directory():
    dest_directory = filedialog.askdirectory(title="Select a directory for sorted files")
    if dest_directory:
        convert_to_double_slash(dest_directory)
    return convert_to_double_slash(dest_directory)


def convert_to_double_slash(directory_path):
    parts = directory_path.split("/")
    return "//".join(parts)




