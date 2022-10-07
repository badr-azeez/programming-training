#!/usr/bin/python3

a = [2, 6, -7]

def largest(lists):
    large_number = lists[0]
    for num in lists:
        if num > large_number:
            large_number = num
    return large_number

print(largest(a))
