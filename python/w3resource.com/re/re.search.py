#!/usr/bin/python3

import re
'''
Scan through string looking for a match to the pattern, returning
    a first Match object, or None if no match was found.
'''

print('='*20,'Example 1','='*20)
ex1 = re.search(r'badr','i am badr')
print(ex1.group())


print('='*20,'Example 2','='*20)
ex2 = re.search(r'\d\d\d','iraq313414') # first Match object
print(ex2.group())  

print('='*20,'Example 3','='*20)
ex3 = re.search(r'\w\w\w','iraq313414')
print(ex3.group())

print('='*20,'Example 4','='*20)
ex4 = re.search(r'..i','123ggi') # The Dot Matches (Almost) Any Character
print(ex4.group())

print('='*20,'Example 5','='*20)
ex5 = re.search(r'pi+','pepiii124') # one or more
print(ex5.group())

print('='*20,'Example 7','='*20)
ex7 = re.search(r'\d\s*\d\s*\d','ba1  2  3dd') # zero or more
print(ex7.group())

print('='*30,'Example 8','='*30)
ex8 = "my email is badr-az@gmail.com  skill pro"
re1 = re.search(r'\w+@\w+',ex8)
re2 = re.search(r'[\w-]+@[\w.-]+',ex8)
re3 = re.search(r'([\w-]+)@([\w.-]+)',ex8)
print(re1.group())
print(re2.group())
print('---')
print(re3.group(0))
print(re3.group(1))
print(re3.group(2))

print('='*30,'Example 9','='*30)
ex9 = 'hello i am badr'
re4 = re.search(r'\w+(?=\sbadr)',ex9) # search the word badr  and return before the  pattern \w+
print(re4.group())

print('='*30,'Example 10','='*30)
re5 = re.search('^<html>','\n<html>',re.MULTILINE)
print(re5.group())

print('='*30,'Example 11','='*30)
patterns = ['this','that','badr','text']
text     = 'Does this text match the pattern?'

for pattern in patterns:
    print('looking for %s in %s --> '%(pattern,text),end='')
    if re.search(pattern,text):
        print('found a match')
    else:
        print('not match')