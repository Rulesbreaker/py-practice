# -*- coding: utf-8 -*-

s = input('Please input your age:')
age = int(s)
if age >= 18:
    print('your age is:', age)
    print('you are a adult')
elif age >= 6:
    print('your age is:', age)
    print('you are a teenager')
else:
    print('your age is:', age)
    print('you are a kid')