#!/usr/bin/python3

def htmlword(tag,string):
    return '<%s>%s</%s>' % (tag,string,tag)

print(htmlword('i','python'))

print(htmlword('b','Title'))