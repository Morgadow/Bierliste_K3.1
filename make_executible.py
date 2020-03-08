#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import os
import shutil
from Bierliste_Tool import __version__
import time

PROJECT_NAME = "Bierliste_Tool"

print("Create .exe file for version: " + __version__)
print("")

if not os.path.exists(os.path.join("Executible", 'v' + __version__)):
    print("Preparing folder " + 'v' + __version__)
    os.makedirs(os.path.join("Executible", 'v' + __version__))
    shutil.copyfile("Example_file.xlsx", os.path.join("Executible", 'v' + __version__, "Example_file.xlsx"))
    shutil.copyfile("settings.ini", os.path.join("Executible", 'v' + __version__, "settings.ini"))
else:
    print("Folder already exists, file will be replaced!")
    if os.path.exists(os.path.join("Executible", 'v' + __version__, "{}.exe".format(PROJECT_NAME))):
        os.remove(os.path.join("Executible", 'v' + __version__, "{}.exe".format(PROJECT_NAME)))

print("\nMake executible:")
os.system("make_executible.bat")

# give programm some time to finish task
time.sleep(5)

print("\nCleaning up ...")
shutil.copyfile(os.path.join("dist", "{}.exe".format(PROJECT_NAME)), os.path.join("Executible", 'v' + __version__, "{}.exe".format(PROJECT_NAME)))
for folder in ('build', 'dist', '__pycache__', '.idea'):
    try:
        shutil.rmtree(folder)
    except:
        pass
os.remove("{}.spec".format(PROJECT_NAME))
