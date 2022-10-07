#!/usr/bin/python3

def dif(nums):
    if len(nums) == len(set(nums)):
        return True
    else:
        return False


print(dif([1,2,3,4,5,4]))
print(dif([1,2,3]))