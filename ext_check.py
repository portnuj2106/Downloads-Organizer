from pathlib import Path

import extensions


def is_video_file(file):
    return Path(file).suffix in extensions.video_extensions


def is_image_file(file):
    return Path(file).suffix in extensions.image_extensions


def is_audio_file(file):
    return Path(file).suffix in extensions.audio_extensions


def is_archive_file(file):
    return Path(file).suffix in extensions.archive_extensions


def is_excel_file(file):
    return Path(file).suffix in extensions.excel_extensions


def is_powerpoint_file(file):
    return Path(file).suffix in extensions.powerpoint_extensions


def is_doc_file(file):
    return Path(file).suffix in extensions.doc_extensions


def is_pdf_file(file):
    return Path(file).suffix == extensions.pdf_extensions


def is_txt_file(file):
    return Path(file).suffix == extensions.txt_extensions


def is_exe_file(file):
    return Path(file).suffix in extensions.exe_extensions


def is_html_file(file):
    return Path(file).suffix in extensions.html_extensions


def is_torrent_file(file):
    return Path(file).suffix in extensions.torrent_extensions