#!/usr/bin/python3

a = ['abc', 'xyz', 'aba', '1221','abc','aba']
d_item = set()
u_item = []
for item in a:
    if item not in d_item:
        d_item.add(item)
        u_item.append(item)
print(u_item)