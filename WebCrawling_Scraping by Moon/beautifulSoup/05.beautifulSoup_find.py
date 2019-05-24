# 05.beautifulSoup_find.py

# find() 함수 사용
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://localhost/index.html"

urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")
# find()를 이용해 tag명, id, class, text를 이용하여 search

print(bs.find("h1"))  # 첫번째 나오는 h1 tag
print(bs.find(id="tiger"))
print(bs.find(class_="lang"))
print(bs.find(text="강아지").parent)


