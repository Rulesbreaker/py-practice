# use_pickle.py
# -*- coding: utf-8 -*-

import pickle

d = dict(name='Bob', age=20, score=88)
f = open('F:/Joey/Code/py-practice/test_samples/pickle.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('F:/Joey/Code/py-practice/test_samples/pickle.txt', 'rb')
d2 = pickle.load(f)
f.close()
print(d2)