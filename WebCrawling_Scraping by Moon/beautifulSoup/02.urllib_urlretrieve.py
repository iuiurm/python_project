# 02.urllib_urlretrieve.py

# 특정 url에 대한 내용을 파일로 저장
from urllib.request import urlretrieve

# 저장하려는 resource에 대한 문자열 생성
url = "http://www.naver.com/index.html"

# 저장하려는 파일경로와 파일명을 문자열로 지정
save_name = "../naver.index.html"

# urlretrieve를 이용해 데이터를 추출한 후 저장
urlretrieve(url, save_name)
print("성공적으로 저장되었습니다.!!")

