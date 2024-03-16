import os
from pathlib import Path
import shutil

import ext_check

os.chdir("C:\\Users\\User\\Downloads")


def organize():
    for file in os.listdir():
        if ext_check.is_video_file(file):
            Path("F:\\Downloads\\Video").mkdir(exist_ok=True)
            shutil.move(file, "F:\\Downloads\\Video")
        elif ext_check.is_image_file(file):
            Path("F:\\Downloads\\Images").mkdir(exist_ok=True)
            shutil.move(file, "F:\\Downloads\\Images")
        elif ext_check.is_audio_file(file):
            Path("F:\\Downloads\\Audio").mkdir(exist_ok=True)
            shutil.move(file, "F:\\Downloads\\Audio")
        elif ext_check.is_archive_file(file):
            Path("F:\\Downloads\\Archives").mkdir(exist_ok=True)
            shutil.move(file, "F:\\Downloads\\Archives")
        elif ext_check.is_excel_file(file):
            Path("F:\\Downloads\\Excel").mkdir(exist_ok=True)
            shutil.move(file, "F:\\Downloads\\Excel")
        elif ext_check.is_powerpoint_file(file):
            Path("F:\\Downloads\\Presentations").mkdir(exist_ok=True)
            shutil.move(file, "F:\\Downloads\\Presentations")
        elif ext_check.is_doc_file(file):
            Path("F:\\Downloads\\Word").mkdir(exist_ok=True)
            shutil.move(file, "F:\\Downloads\\Word")
        elif ext_check.is_pdf_file(file):
            Path("F:\\Downloads\\PDF").mkdir(exist_ok=True)
            shutil.move(file, "F:\\Downloads\\PDF")
        elif ext_check.is_txt_file(file):
            Path("F:\\Downloads\\TXT").mkdir(exist_ok=True)
            shutil.move(file, "F:\\Downloads\\TXT")
        elif ext_check.is_exe_file(file):
            Path("F:\\Downloads\\EXE").mkdir(exist_ok=True)
            shutil.move(file, "F:\\Downloads\\EXE")
        elif ext_check.is_html_file(file):
            Path("F:\\Downloads\\HTML").mkdir(exist_ok=True)
            shutil.move(file, "F:\\Downloads\\HTML")
        elif ext_check.is_torrent_file(file):
            Path("F:\\Downloads\\Torrents").mkdir(exist_ok=True)
            shutil.move(file, "F:\\Downloads\\Torrents")
        else:
            if Path(file).is_file():
                Path("F:\\Downloads\\Other").mkdir(exist_ok=True)
                shutil.move(file, "F:\\Downloads\\Other")


if __name__ == "__main__":
    organize()
