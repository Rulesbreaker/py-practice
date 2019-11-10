# use_itertools.py
# -*- coding: utf-8 -*-

import itertools

naturals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, naturals) 
# print(list(ns))

# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)

# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key, list(group))

def pi(N):
    oddList = itertools.count(1, 2)    
    a, sum = 1, 0
    for n in itertools.takewhile(lambda x: x <= 2 * N - 1, oddList):
        sum = sum + a * 4 / n
        a = - a
    return sum

assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')