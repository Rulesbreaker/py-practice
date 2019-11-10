# -*- coding: utf-8 -*-
import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# print(my_abs('A'))

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# print(move(100, 100, 60, math.pi / 6))

def quadratic(a, b, c):
    for x in (a, b, c):        
        if not isinstance(x, (int, float)):
            raise TypeError('bad operand type')

    temp = b * b - 4 * a * c
    if a != 0 and  temp >= 0:
        x1 = (-b + math.sqrt(temp)) / (2 * a)
        x2 = (-b - math.sqrt(temp)) / (2 * a)
        return x1, x2
    else: 
        return 'Could\'t find a result'
    

print(quadratic(2, 3, 1))