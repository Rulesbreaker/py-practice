# use_collections.py
# -*- coding: utf-8 -*-

# nametuple example
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

# print(p.x, p.y)
# print(isinstance(p, tuple))

# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque example
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.pop()
q.appendleft('y')
# print(q)

# defaultdict example
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])

# OrderedDict example
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
# print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(od)

# ChainMap example
from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])