#!/usr/bin/python3

import re
'''
 will only match at the beginning of the string and not at the beginning of each line.

'''
print('='*20,'Example 1','='*20)
msg = 'badr hello world'
pattern = r"hello"
if re.match(pattern,msg):
    print('match')
else: 
    print('Not Match')

print('='*20,'Example 2','='*20)
result = re.match('\\\\s','\\share') # search for first word in string
print(result.group())
print(result)

print('='*20,'Example 3','='*20)
phoe = ('9999999999','9999999-999','99999999')
for i in phoe:
    if re.match(r'[8-9]{1}[0-9]{9}',i) and len(i) == 10:
        print('Match ',i)