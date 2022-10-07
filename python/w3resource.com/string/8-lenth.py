#!/usr/bin/python3

def lists(list):
    longer = []
    for item in list:
        longer.append(len(item))
    print(max(longer)) 


#lists(['word','bad','hello','programmer','masterbadr1997'])

def listlen(list):
    word_len = []
    for word in list:
        word_len.append((len(word),word))
    word_len.sort()
    return word_len[-1][1] , word_len[-1][0]


print(listlen(['word','bad','hello','programmer','masterbadr1997']))



