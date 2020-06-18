#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import os

DEPENDECIES = ('tkinter', 'openpyxl', 'ConfigParser', 'Pillow')

def install_dep():
    for index, elem in enumerate(DEPENDECIES, 1):
        try:
            print("Installing package {} of {}: {}".format(index, len(DEPENDECIES), elem))
            os.system("pip install {}".format(elem))
        except Exception as e:
            print(e)
