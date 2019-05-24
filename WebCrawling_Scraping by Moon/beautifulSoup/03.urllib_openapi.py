# 03.urllib_urlopenapi.py

# open api를 이용해서 데이터 추출
from urllib.request import urlopen
from urllib.parse import urlencode
# open api의 url (영화진흥위원회 boxoffice 순위)
open_api_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml"

# open api를 호출하기 위한 매개변수
open_api_param = {
    "key": "430156241533f1d058c603178cc3ca0e",
    "targetDt": "20190314"
}
# urlencoder를 이용하여 완성된 url생성
params = urlencode(open_api_param)

# 요청 url 생성 > 접속 > 결과 데이터 추출 > 출력
url = open_api_url + "?" + params
data = urlopen(url).read().decode("utf-8")
print(data)

