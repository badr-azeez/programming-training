#!/usr/bin/python3

def histgm(numbers):
    for n in numbers:
        out = ''
        while(n > 0):
            out += '*'
            n -= 1

        print(out)


histgm([1,2,3,4,5,4,3,2,1])
