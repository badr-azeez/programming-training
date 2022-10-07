#!/usr/bin/python3

#exm 1 
def addation(n):
    return n + n

numbers = [1,2,3,4]

print(list(map(addation,numbers)))

#exm 2
val = input('Enter X & Y : ')

x,y = map(int,val.split())
print('Values is ',x,y)