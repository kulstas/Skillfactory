from bs4 import BeautifulSoup
from urllib.request import urlopen

url = [
    'https://shop.magazin-poliva1.ru/catalog/good/2f91d609-e7a6-11ee-9797-3cecef238a51/',
]

file = open('content.txt', 'a')

for x in url:
    html_code = str(urlopen(x).read(), 'utf-8')
    soup = BeautifulSoup(html_code, 'html.parser')

    