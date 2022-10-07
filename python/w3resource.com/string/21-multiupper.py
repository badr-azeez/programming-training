#!/usr/bin/python3

def strupper(str):
    str_up = 0

    for letter in str:
        if letter.upper() == letter:
            str_up += 1
    if str_up >= 2 :
        return str.upper()
    return str

print(strupper('python'))
print(strupper('pythON'))
