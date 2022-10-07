#!/usr/bin/python3

import re
"""Return a list of all non-overlapping matches in the string.

    If one or more capturing groups are present in the pattern, return
    a list of groups; this will be a list of tuples if the pattern
    has more than one group.

    Empty matches are included in the result."""

string = 'Badr Is live in iraq badr also like to be programmer'

print('='*30,'Example 1','='*30)
res1 = re.findall(r'.',string) # return any single character
print(res1)

print('='*30,'Example 2','='*30)
res2 = re.findall(r'\w',string) # return letters
print(res2)

print('='*30,'Example 3','='*30)
res3 = re.findall(r'\w*',string) # return any single or words
print(res3)

print('='*30,'Example 4','='*30)
res4 = re.findall(r'\w+',string) # return  words
print(res4)

print('='*30,'Example 5','='*30)
res5 = re.findall(r'^\w+',string) # return first  words
print(res5)

print('='*30,'Example 6','='*30)
res6 = re.findall(r'\w+$',string) # return first  words
print(res6)

print('='*30,'Example 7','='*30)
res7 = re.findall(r'@\w+.(\w+)','badr@gmail.com badr@gmail.co badr@gmail.in \
    badr@gmail.edu badr@gmail.org') # return ext  words
print(res7)

print('='*30,'Example 8','='*30)
res8 = re.findall(r'\d{2}-\d{2}-\d{4}','April 6 2020 20-10-2020 2020-03-3') # return first  words
print(res8)