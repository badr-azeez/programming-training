#!/usr/bin/python3

while True:
    try:
        x  = int(input('Enter Number'))
        print(x)
    except ValueError:
        print('Number Wronge Try Again')
