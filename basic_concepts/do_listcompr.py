# -*- coding: utf-8 -*-
L = [x * x for x in range(1, 11) if x % 2 == 0]
M = [m + n for m in 'ABC' for n in 'XYZ']
N = ['Hello', 'World', 18, 'Apple', None]
N1 = [s.lower() for s in N if(isinstance(s, str))]

print(N1)