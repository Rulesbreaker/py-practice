# -*- coding: utf-8 -*-

t=(1,2)
print(t)

t=()
print(t)

t=('a', 'b', ['A', 'B'])
t[2][0]='X'
t[2][1]='Y'
print(t)


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])