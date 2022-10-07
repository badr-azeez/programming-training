#!/usr/bin/python3

def replacechar(str):
    char = str[0]
    str  = str.replace(char,'$')
    str  = char + str[1:]
    return str


print(replacechar('badbr'))