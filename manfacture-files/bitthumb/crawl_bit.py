import requests
from bs4 import BeautifulSoup

url = 'https://www.bithumb.com/'
response  = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

results = soup.find_all('span', class_='blind')
results2 = soup.select_one('strong[class = sort_real]') # 하나만 뽑겠음. 속성 형태
results3 = soup.select('strong[class = sort_real]') # list 형태

# 2번 크롤링 되는 이유는 크롤링 Tag의 문제
# tag를 더 정확한걸 가져오면 문제 해결됨. 지금 현재
#2번 반복되는중.

index = 0
# for result in results :
#     index += 1
#     # 검색된 태그에서 a 태그에서 텍스트를 가져옴
#     #print(index , result.text)

for results2 in results3 :
    print(results2.text)