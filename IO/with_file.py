# with_file.py
# -*- coding: utf-8 -*-

# try:
#     f = open('F:/Joey/Code/py-practice/hello.py', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

with open('F:/Joey/Code/py-practice/test_samples/test.txt', 'r') as f:
    # for line in f.readlines():
    #     print(line.strip())
    s = f.read()
    print(s)
    



