#!/usr/bin/python3

t = (1,2,3,4,5,6)
print(t)
t = t +(7,)
print(t)
t = t[:4] + (100,) + t[:4]
print(t)
print('######## two way')
t = list(t)
print(t)
t.append(22)
t = tuple(t)
print(t)