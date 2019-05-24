# 01.urllib_urlopen.py

# 특정 url의 html을 읽은 후 html의 내용을 출력
from urllib.request import urlopen

# url에 접속한 후 접속객체 생성
urlObj = urlopen("http://localhost/index.html")
# urlObj = urlopen("http://www.naver.com")

# 접속객체를 이용해 HTML을 읽어오고 utf-8로 decoding
print(urlObj.read().decode("utf-8"))

