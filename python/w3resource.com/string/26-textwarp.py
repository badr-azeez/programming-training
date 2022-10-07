#!/usr/bin/python3

import textwrap
simple_text = '''Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java.'''
print(textwrap.fill(simple_text,50))