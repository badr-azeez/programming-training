#!/usr/bin/python3

def strrev(str):
    if len(str) <= 4:
        return ''.join(reversed(str))
    return str


print(strrev('badr'))
print(strrev('python'))