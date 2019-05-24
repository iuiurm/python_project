# 10.beautifulSoup_RottenTomatoes.py

# RottenTomatoes의 연도별 영화 순위를 retrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.rottentomatoes.com/top/bestofrt/?year=2018"

urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")

tr_list = bs.select("#top_movies_main > div > table > tr")

for tr in tr_list:
    print(tr.select_one("td:nth-of-type(3) > a").text.strip())
