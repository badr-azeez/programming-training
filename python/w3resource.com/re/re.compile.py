#!/usr/bin/python3

import re
"""Compile a regular expression pattern, returning a Pattern object."""

email = re.compile('[a-z0-9-]+@[a-z0-9\.-]+')
print(email.findall('badr@gmail.com  badr  azeez '))