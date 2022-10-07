#!/usr/bin/python3

import re
"""Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the Match object and must return
    a replacement string to be used."""

print('='*20,'Example 1','='*20)
str1 = "Cillum commodo nostrud labore minim occaecat nisi."
print(re.sub(r'minim','1111',str1))



print('='*20,'Example 2','='*20)
str1 = "Cillum,commodo,nostrud,labore,minim,occaecat,nisi.;yes"
print(re.sub(r'[,.;]',' ',str1))

print('='*20,'Example 3','='*20)
str1 = "Cillum,commodo,nostrud,labore,minim,occaecat,nisi.;yes"
print(re.sub(r'[,.;]',' ',str1))

print('='*20,'Example 4','='*20)
print(re.sub(r'[0-9]','__','I like 1 and 2'))

print('='*20,'Example 5','='*20)
print(re.sub(r'#.*$','','+964-785-111-2222 # MY PHONE NUMBER'))

print('='*20,'Example 5','='*20)
str1 = 'purple badr@google.com, blah az az@abc.com blah dishwasher'
print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str1))


