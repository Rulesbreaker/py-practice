# do_bytesio.py
# -*- coding: utf-8 -*-

from io import BytesIO

f = BytesIO('中文'.encode('utf-8'))
print(f.read())