#!/usr/bin/python3

def midstr(sep,str):
    return sep[:2]+ str + sep[2:]

print(midstr('<<>>','badr'))
print(midstr('[[]]','badr'))
print(midstr('{{}}','badr'))    