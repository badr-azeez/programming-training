#!/usr/bin/python3

import os,time

print('File :', __file__)
print('TIme Access :' , time.ctime(os.path.getatime(__file__)))
print('Time Modified', time.ctime(os.path.getmtime(__file__)))
print('Time Create', time.ctime(os.path.getctime(__file__)))