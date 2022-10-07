#!/usr/bin/python3

def not_poor(str):
    snot = str.find('not')
    spoor = str.find('poor')
    if spoor > snot and snot>0 and spoor>0:
        return str.replace(str[snot:(spoor+4)],'good')
    else:
        return str

print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))
