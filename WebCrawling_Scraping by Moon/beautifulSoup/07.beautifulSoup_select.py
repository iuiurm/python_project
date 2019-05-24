# 07.beautifulSoup_select.py

# select() 함수 사용
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://localhost/index.html"

urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")

# select_one()은 1개, select()는 list를 return
# select()는 CSS selector를 이용하여 Element를 찾는다.
print(bs.select_one("#tiger").get_text())

li_list = bs.select("div > ul > li")
for li in li_list:
    print(li.text)

print(bs.select("div:nth-of-type(2) > ol > li.lang"))

