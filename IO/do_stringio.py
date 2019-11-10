# do_stringio.py
# -*- coding: utf-8 -*-

from io import StringIO

# f = StringIO()
# f.write('Hello')
# f.write(' ')
# f.write('World!')
# print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')

while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

