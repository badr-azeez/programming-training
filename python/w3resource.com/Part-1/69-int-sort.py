#!/usr/bin/python3

x = int(input('X :'))
y = int(input('Y :'))
z = int(input('Z :'))

s1 = min(x,y,z)
s3 = max(x,y,z)
s2 = (x + y + z) - s1 - s3
print('Order Sort :',s1,s2,s3)