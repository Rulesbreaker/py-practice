# -*- coding: utf-8 -*-
# from collections import Iterable 

d = {'a': 1, 'b': 2, 'c': 3}

# for key in d:
#     print(d.get(key))

# print(isinstance('abc', Iterable))

def findMinAndMax(L):
    max = L[0]
    min = L[0]
    for n in L:
        if n > max:
            max = n
        if n < min:
            min = n
    return (min, max)

print(findMinAndMax([1, 2, 7, 10, -1]))

