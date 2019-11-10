# do_dir.py
# -*- coding: utf-8 -*-

import os

# print(os.name, os.environ.get('PATH'))
# print(os.path.abspath('.'))
# print(os.path.join(r'F:/Joey/Code/py-practice', 'testdir'))
# os.mkdir(r'F:/Joey/Code/py-practice/testdir')
# os.rmdir(r'F:/Joey/Code/py-practice/testdir')
# print(os.path.split('F:/Joey/Code/py-practice/test_samples/test.txt'))
# print(os.path.splitext('F:/Joey/Code/py-practice/test_samples/test.txt'))
print([x for x in os.listdir('.') if os.path.isdir(x)])