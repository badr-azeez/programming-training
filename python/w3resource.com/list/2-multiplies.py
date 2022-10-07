#!/usr/bin/python3

a = [2,2,5]
def multiplies(list):
    final = 1
    for num in list:
        final *= num
    return final

print(multiplies(a))