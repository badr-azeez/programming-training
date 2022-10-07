#!/usr/bin/python3

import collections

def nchar(str):
    return  collections.Counter(str)

print(nchar('hello world'))

print("--"*10)
# 2

def freq_char(str):

    dict = {}
    for n in str:
        keys = dict.keys()
        if n  in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


print(freq_char('hello world'))