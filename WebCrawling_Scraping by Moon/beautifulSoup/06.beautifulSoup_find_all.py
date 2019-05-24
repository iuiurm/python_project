# 06.beautifulSoup_find_all.py

# find_all() 함수 사용
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://localhost/index.html"

urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")

# find_all()은 조건에 부합하는 모든 element를 찾는다.
li_list = bs.find_all("li")
for li in li_list:
    print(li.text)

a_list = bs.find_all("a")
for a in a_list:
    print(a.attrs["href"])

