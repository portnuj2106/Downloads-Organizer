import os
from pathlib import Path
import shutil

import ext_check

from get_directories import get_directory, get_dest_directory

directory = get_directory()

dest_directory = get_dest_directory()

os.chdir(directory)


def organize():
    for file in os.listdir():
        if ext_check.is_video_file(file):
            Path(f"{dest_directory}\\Video").mkdir(exist_ok=True)
            shutil.move(file, f"{dest_directory}\\Video")
        elif ext_check.is_image_file(file):
            Path(f"{dest_directory}\\Images").mkdir(exist_ok=True)
            shutil.move(file, f"{dest_directory}\\Images")
        elif ext_check.is_audio_file(file):
            Path(f"{dest_directory}\\Audio").mkdir(exist_ok=True)
            shutil.move(file, f"{dest_directory}\\Audio")
        elif ext_check.is_archive_file(file):
            Path(f"{dest_directory}\\Archives").mkdir(exist_ok=True)
            shutil.move(file, f"{dest_directory}\\Archives")
        elif ext_check.is_excel_file(file):
            Path(f"{dest_directory}\\Excel").mkdir(exist_ok=True)
            shutil.move(file, f"{dest_directory}\\Excel")
        elif ext_check.is_powerpoint_file(file):
            Path(f"{dest_directory}\\Presentations").mkdir(exist_ok=True)
            shutil.move(file, f"{dest_directory}\\Presentations")
        elif ext_check.is_doc_file(file):
            Path(f"{dest_directory}\\Word").mkdir(exist_ok=True)
            shutil.move(file, f"{dest_directory}\\Word")
        elif ext_check.is_pdf_file(file):
            Path(f"{dest_directory}\\PDF").mkdir(exist_ok=True)
            shutil.move(file, f"{dest_directory}\\PDF")
        elif ext_check.is_txt_file(file):
            Path(f"{dest_directory}\\TXT").mkdir(exist_ok=True)
            shutil.move(file, f"{dest_directory}\\TXT")
        elif ext_check.is_exe_file(file):
            Path(f"{dest_directory}\\EXE").mkdir(exist_ok=True)
            shutil.move(file, f"{dest_directory}\\EXE")
        elif ext_check.is_html_file(file):
            Path(f"{dest_directory}\\HTML").mkdir(exist_ok=True)
            shutil.move(file, f"{dest_directory}\\HTML")
        elif ext_check.is_torrent_file(file):
            Path(f"{dest_directory}\\Torrents").mkdir(exist_ok=True)
            shutil.move(file, f"{dest_directory}\\Torrents")
        else:
            if Path(file).is_file():
                Path(f"{dest_directory}\\Other").mkdir(exist_ok=True)
                shutil.move(file, f"{dest_directory}\\Other")


if __name__ == "__main__":
    organize()
