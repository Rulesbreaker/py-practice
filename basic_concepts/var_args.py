# -*- coding: utf-8 -*-

def power(x, n=2):
    sum = 1
    while n > 0:
        sum = sum * x
        n = n - 1
    return sum

# print(power(5, 1))

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

# enroll('Sarah', 'F', city='Chongqing')

def add_end(L=None):
    if L is None:
        L = []    
    L.append('END')
    print(L) 
    return L

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]
# print(calc(1, 2, 5, 7))
print(calc(*nums))

