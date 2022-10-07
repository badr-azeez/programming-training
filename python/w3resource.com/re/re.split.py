#!/usr/bin/python3

import re
'''
Split the source string by the occurrences of the pattern,
    returning a list containing the resulting substrings.  If
    capturing parentheses are used in pattern, then the text of all
    groups in the pattern are also returned as part of the resulting
    list.  If maxsplit is nonzero, at most maxsplit splits occur,
    and the remainder of the string is returned as the final element
    of the list.
'''
print('='*20,'Example 1','='*20)
print(re.split(r'i','Analytics'))



print('='*20,'Example 2','='*20)
print(re.split(r'y','Analytics Done'))


print('='*20,'Example 3','='*20)
print(re.split(r'y','Analytics Vidhya',maxsplit=1))


print('='*20,'Example 4','='*20)
myList = 'Apple,Microsoft,Android Linux;Windows'
print(re.split(r'[;, ]',myList))


print('='*20,'Example 5','='*20)
mystr = 'Apple      Microsoft        Android  Linux  Windows'
print(re.split(r'\s+',mystr)) #  split by spaces
