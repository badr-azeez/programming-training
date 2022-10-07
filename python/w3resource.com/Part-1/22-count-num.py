#!/usr/bin/python3

def list_n(lst,num):
    count = 0
    for n in lst:
        if n == num:
            count = count + 1
    return count


list_1 = [1,2,5,6,7,4,3]
list_2 = [1,4,6,7,4,3,7,34,4]

print( list_n(list_1,4) )

print( list_n(list_2,4) )