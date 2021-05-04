import urllib.request
import json

r = urllib.request.urlopen('http://httpbin.org/get')
# 读取response的内容
text = r.read()
# http返回状态码和msg
print(r.status, r.reason)

# 返回的内容是json格式，直接用loads函数加载
obj = json.loads(text)
print(obj)

# r.headers是一个HTTPMessage对象
print(r.headers)
for k,v in r.headers._headers:
    print('%s: %s' % (k, v))

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
# 添加自定义的头信息
req = urllib.request.Request('http://httpbin.org/user-agent')
req.add_header('User-Agent', ua)
# 接受一个urllib.request.Request对象作为参数
r = urllib.request.urlopen(req)
resp = json.load(r)
# 打印出httpbin网站返回信息里的user-agent
print("user-agent: ", resp["user-agent"])


# auth_handler = urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='httpbin realm',
#                           uri='http://httpbin.org/basic-auth/guye/123456',
#                           user='guye',
#                           passwd='123456')
# opener = urllib.request.build_opener(auth_handler)
# urllib.request.install_opener(opener)
# r = urllib.request.urlopen('http://httpbin.org')
# print(r.read().decode('utf-8'))

# 使用GET参数
params = urllib.parse.urlencode({'spam':1, 'eggs':2, 'bacon':2})
url = 'http://httpbin.org/get?%s' % params
with urllib.request.urlopen(url) as f:
    print(json.load(f))

# 使用POST方法传递参数
data = urllib.parse.urlencode({'name': '小明', 'age':2})
data = data.encode()
with urllib.request.urlopen('http://httpbin.org/post', data) as f:
    print(json.load(f))


# 使用代理IP请求远程url
# proxy_handler = urllib.request.PxoxyHandler({'http': 'http://iguye.com:41801'})
# opener = urllib.request.build_opener(proxy_handler)
# opener.open('http://httpbin.org/ip')
# print(r.read())