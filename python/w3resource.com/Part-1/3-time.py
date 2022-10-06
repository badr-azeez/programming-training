#!/usr/bin/python3
from datetime import datetime
print('Current data and time')
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
hour = datetime.now().hour
minute = datetime.now().minute
second = datetime.now().second
print( year, '-', month, '-', day,'-', ' ',hour,':', minute,':', second,sep='')

print('-' * 9)

now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
