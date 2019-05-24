# 04.beautifulSoup_basic.py

# BeautifulSoup4 library이용 : HTML Parser Library
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://localhost/index.html"

urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(),"html.parser")

print(bs.html.body.h1)
print(bs.html.body.h1.text)
print(bs.html.body.h1["id"])

print(bs.li)
print(bs.li.next_sibling.next_sibling)

