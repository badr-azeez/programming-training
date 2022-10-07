#!/usr/bin/python3

import collections, pprint

f = open('abc.txt','r')
count = collections.Counter(f.read())
value = pprint.pformat(count)
print(value)