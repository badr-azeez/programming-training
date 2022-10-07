#!/usr/bin/python3

def new_str(str):
    if len(str) >= 2 and str[:2] == 'Is':
        return str
    return 'Is ' + str

print(new_str('empty?'))
print(new_str('Is he Badr?'))

