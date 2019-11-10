# -*- coding: utf-8 -*-

s = set([1, 2, 2, 3, 3])
s.add(4)
# print(s)

s.remove(4)
# print(s)

s1 = set([1, 2, 3])
s2 = set([1, 3, 4])
print(s1 & s2, s1 | s2)
