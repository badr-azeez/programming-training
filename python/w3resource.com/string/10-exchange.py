#!/usr/bin/python3

def string(str):
    return str[-1:] + str[1:-1] + str[:1]

print(string('programmer'))