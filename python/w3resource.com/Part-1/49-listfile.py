#!/usr/bin/python3

import os

list_d = [f for f in os.listdir() if os.path.isfile(f)]

print(list_d)