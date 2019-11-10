# -*- coding: utf-8 -*-

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# person('Bob', 35, city='Beijing')

extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, city=extra['city'], job=extra['job'])
# person('Jack', 24, **extra)

def person1(name, age, *, city, job='Engineer'):
    print(name, age, city, job)

# person1('Jack', 24, city='Beijing')

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2, 3, 'a', 'b', X=11, Y=22, s=True)