from lxml import etree

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

selector = etree.HTML(html_doc)
# 取出页面内所有的链接
links = selector.xpath('//p[@class="story"]/a/@href')
for link in links:
    print(link)

html_bookstore = """
<?xml version="1.0" ?>
<bookstore>

<book category="cooking">
    <title lang="en">Everyday Italian</title>
    <author>Ciada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
</book>

<book category="children">
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2015</year>
    <price>29.99</price>
</book>

<book category="web">
    <title lang="en">XQuery Kick Start</title>
    <author>James McGovern</author>
    <author>Per Bothner</author>
    <author>Kurt Cagle</author>
    <author>James Linn</author>
    <year>2003</year>
    <price>49.99</price>
</book>

<book category="web" cover="paperback">
    <title lang="en">Learning XML</title>
    <author>Eric T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
</book>
</bookstore>
"""

se = etree.HTML(html_bookstore)
print(se.xpath('//book'))
# 选取书店下所有的书本的作者的名字
print(se.xpath('//bookstore/book/author/text()'))
# 选取书店所有的书本的语言
print(se.xpath('//bookstore/book/title/@lang'))

# 选取书店下第一本书的标题
print(se.xpath('//bookstore/book[1]/title/text()'))
# 选取书店下最后一本书的标题
print(se.xpath('//bookstore/book[last()]/title/text()'))
# 选取书店下倒数第二本书的标题
print(se.xpath('//bookstore/book[last()-1]/title/text()'))
# 选取书店下前两本书的标题
print(se.xpath('//bookstore/book[position()<3]/title/text()'))
# 选取所有分类为web的书本
print(se.xpath('//book[@category="web"]/title/text()'))
# 选取所有价格大于30.00元的书本
print(se.xpath('//book[price>30.00]/price/text()'))
