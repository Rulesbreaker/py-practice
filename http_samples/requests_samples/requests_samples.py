import requests
from requests.models import requote_uri

# GET请求
r = requests.get('http://httpbin.org/get')
print('GET请求', r.status_code, r.reason)
print(r.text)

# 带参数的GET请求
r = requests.get('http://httpbin.org/get', params={'a': '1', 'b': '2'})
print('带参数的GET请求', r.json())

# POST请求
r = requests.post('http://httpbin.org/post', data={'a': '1'})
print('POST请求', r.json())

# ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \ 
#     'AppleWebKit/537.36 (KHTML, like Gecko) ' \
#     'Chrome/87.0.4280.88 Safari/537.36'

#自定义headers请求
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
headers = {'User-Agent': ua}
r = requests.get('http://httpbin.org/headers', headers=headers)
print('自定义headers请求', r.json())

# 带cookies的请求
cookies = dict(userid='123456', token='xxxxxxxxxx')
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print('带cookies的请求', r.json())

# Basic-auth认证请求
r = requests.get('http://httpbin.org/basic-auth/guye/123456',auth=('guye','123456'))
# print(r.text)
print('Basic-auth认证请求', r.json())

# 主动抛出状态码异常
bar_r = requests.get('http://httpbin.org/status/404')
print(bar_r.status_code)
bar_r.raise_for_status();

# 使用requests.Session对象请求
s = requests.Session()
s.get('http://httpbin.org/cookies/set/userid/123456789')
s.get('http://httpbin.org/cookies/set/token/xxxxxxxxxxxxxx')
r = s.get('http://httpbin.org/cookies')
print('检查session中的cookies', r.json())

# 在requests中使用代理
print('不使用代理', requests.get('http://httpbin.org/ip').json())
#print('使用代理', requests.get('http://httpbin.org/ip', proxies={'http': 'http://iguye.com:41801'}).json())

# 使用timeout参数
r = requests.get('http://httpbin.org/delay/4', timeout=5)
print(r.text)