#!/usr/bin/python3

items = input("Input comma separated sequence of words :")

word = [word for word in items.split(',')]

print(','.join(sorted(set(word))) )