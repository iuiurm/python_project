#naver 에서 html 파일을 가지고 온다.
# beautiful soup 를 이용해서 parsing
# 실시간 검색어 10위 까지 출력.

import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
response  = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

results = soup.find_all('span', class_='ah_k')
# 2번 크롤링 되는 이유는 크롤링 Tag의 문제
# tag를 더 정확한걸 가져오면 문제 해결됨. 지금 현재
#2번 반복되는중.
print(results)

index = 0
for result in results :
    index += 1
    # 검색된 태그에서 a 태그에서 텍스트를 가져옴
    print(index , result.text)

