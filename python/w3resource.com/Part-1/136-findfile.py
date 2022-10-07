#!/usr/bin/python3

import os

dirs = os.listdir()
print([file for file in dirs if os.path.isfile(file) and file == '112-del.py'])
