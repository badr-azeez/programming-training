#!/usr/bin/python3

def oddstr(str):
    string = ''
    for n in range(len(str)):
        if n % 2 == 0:
            string += str[n]
    return string

print(oddstr('badr'))