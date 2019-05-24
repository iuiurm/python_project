# 11.beautifulSoup_RottenTomatoes.py

# Daum 영화 페이지에서 특정 영화의 사용자 ID, 평점, Comment 추출
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://movie.daum.net/moviedb/grade?movieId=101393&type=netizen&page=2"

urlObj = urlopen(url)

bs = BeautifulSoup(urlObj.read(), "html.parser")
#mArticle > div.detail_movie.detail_rating > div.movie_detail > div.main_detail > ul > li:nth-child(5) > div
li_list = bs.select("#mArticle > div.detail_movie.detail_rating > div.movie_detail > div.main_detail > ul > li")
#mArticle > div.detail_movie.detail_rating > div.movie_detail > div.main_detail > ul > li:nth-child(5) > div > a > em
for item in li_list:
    print(item.select("div > a > em")[0].text.strip(), end=" - ")
    print(item.select("div div > em")[0].text.strip(), end=" - ")
    print(item.select("div > p")[0].text.strip())


