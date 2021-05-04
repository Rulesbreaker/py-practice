import bs4
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# 创建一个BeautifulSoup对象
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.stirng)
print(soup.title.string)
print(soup.a)
# 取出第一个a标签所有的属性
print(soup.a.attrs)
print(soup.a.attrs['href'])
# 判断是否有class属性q
soup.a.has_attr('class')
# 取出第一个p标签下的所有子节点
print(soup.p.children)
# 取出来的结果是一个迭代器，所以用list转换一下
print(list(soup.p.children))
print(list(soup.p.children)[0])
print(list(soup.p.children)[0].text)

# 取出本页面内所有的链接
print(soup.find_all('a'))

# 取出id=link3的那个节点
print(soup.find(id='link3'))
# 取出页面内所有的文本
print(soup.get_text())

# 支持CSS选择器
# 查找类名为story的节点
soup.select('.story')
# 查找id=link3的节点
soup.select('#link3')


soup_lxml = BeautifulSoup(html_doc, 'lxml')
print('##' * 10, soup_lxml.a)
