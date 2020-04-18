#! /usr/bin/python3

import sys
import os
from pathlib import Path

MARK = sys.argv[1]
MARKED_DIR = os.getcwd()
MMKK_DIR = Path(os.path.dirname(os.path.realpath(__file__)))

def do_work():
    """Do the work."""

    list_filename = MMKK_DIR / ".kk.lst"

    ligne = f"{MARK}@{MARKED_DIR}\n"

    with open(list_filename,'a') as list_file:
        list_file.write(ligne)

    # Création du raccourcis dans konqueror
    generic_file = MMKK_DIR / "generic.desktop"
    current_content = open(generic_file, "r").read()
    new_content = current_content.replace("KKK", MARK).replace("RRR", MARKED_DIR)

    new_filename = Path.home() \
                / f".local/share/kservices5/searchproviders/{MARK}.desktop"

    with open(new_filename,'w') as new_file:
        new_file.write(new_content)

do_work()
