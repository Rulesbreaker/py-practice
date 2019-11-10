# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# print([L[0], L[1], L[2]])

r = []
n = 3
for i in range(n):
    r.append(L[i])

# print(L[::2])
# print('abcdefg'[::3])

def trim(s):
    if s[:1] == ' ':
        return trim(s[1:])
    elif s[-1:] == ' ':
        return trim(s[:-1])
    else:
        return s

print(trim('    '))