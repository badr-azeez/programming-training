#!/usr/bin/python3

def chrse(str):
    if len(str) >= 2:
        l = str[0:2]
        r = str[len(str) - 2 : len(str)]
        return l+r
    else:
        return 'Empty'

print(chrse('w3resource'))

print("--"*10)

#2
def chars(str):
    if len(str) < 2:
        return ''
    return str[:2] + str[-2:]

print(chars('w3resource'))
