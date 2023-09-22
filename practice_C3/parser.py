import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree
import xml.etree.ElementTree as ET

# создадим объект ElementTree. Он возвращается функцией parse()
parser = lxml.etree.HTMLParser()
tree = lxml.etree.parse('Welcome to Python.org.html', parser)  # попытаемся спарсить наш файл с помощью html-парсера. Сам html - это то, что мы скачали и поместили в папку из браузера.

ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')  # помещаем в аргумент метода findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)

# создаём цикл, в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т. е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тэг <a>)
    time = li.find('time')
    print(f'Новость: {a.text} — ', time.get('datetime'))  # из этого тега забираем текст, это и будет нашим названием

# ===

# html = requests.get('https://www.python.org/').content

# html = ''' <html>
#  <head> <title> Some title </title> </head>
#  <body>
#   <tag1> some text
#      <tag2> MY TEXT </tag2>
#    </tag1>
#  </body>
# </html>
# '''
#
# tree = lxml.html.document_fromstring(html)
# # title = tree.xpath('/html/head/title/text()')
# tag2 = tree.xpath('/html/body/tag1/tag2/text()')
#
# print(tag2)