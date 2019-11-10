# -*- coding: utf-8 -*-

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Joey'] = 98
# print(d)

d['Jack'] = 77
# print(d)

d['Jack'] = 88
# print(d)

# print(d.get('Sara', -1))

d.pop('Bob')
print(d)

