#!/usr/bin/python3

a = {0:10,1:20}
print(a)
a[2] = 20
print(a)
# or
a.update({4:40})
print(a)
a.update({4:40,0:9})
print(a)

