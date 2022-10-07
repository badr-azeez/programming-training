#!/usr/bin/python3

def edit(str):
    string = str[-3:]
    if len(str) >= 3:
        if string == 'ing':
            return str + 'ly'
        else:
            return str + 'ing'
    else:
        return str

print(edit('ac'))
print(edit('abc'))
print(edit('string'))
