#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import os

DEPENDECIES = ('setuptools', 'tkintertable', 'openpyxl', 'ConfigParser', 'Pillow')

def install_dep():

    # update pip
    os.system("python -m pip install --upgrade pip")

    for index, elem in enumerate(DEPENDECIES, 1):
        try:
            print("Installing package {} of {}: {}".format(index, len(DEPENDECIES), elem))
            os.system("pip install {}".format(elem))
        except Exception as e:
            print(e)
