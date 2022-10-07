#!/usr/bin/python3

d = {1: 10, 2: 20, 'd': 30, 4: 40, 5: 50, 6: 60}


def check_key(v, d):
    if v in d:
        print('Exist:', d[v])
    else:
        print('Not Exist:', v)


check_key(6, d)
check_key(2, d)
check_key(622, d)
check_key('d', d)
