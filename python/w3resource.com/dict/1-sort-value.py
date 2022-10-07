#!/usr/bin/python3

import operator

num = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_d = sorted(num.items(),key=operator.itemgetter(0))
print('ascending',sorted_d)
sorted_d_rev = sorted(num.items(),key=operator.itemgetter(0),reverse= True)
print('descending',sorted_d_rev)
