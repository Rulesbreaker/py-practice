# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))
print(classmates[2], classmates[-1])

classmates.append('Adam')
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)

classmates[1] = 'Sarah'
print(classmates)

classmates[2] = ['Apple', 123, True]
print(classmates)
print(classmates[2][1])