# 09.beautifulSoup_boxoffice.py

# 영화진흥위원회의 Open API를 이용하여 특정날짜의 boxoffice순위를 retrieve
from urllib.request import urlopen
from urllib.parse import urlencode
from bs4 import BeautifulSoup

open_api_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml"
open_api_params = {
    "key": "430156241533f1d058c603178cc3ca0e",
    "targetDt": "20190314"
}
url = open_api_url + "?" + urlencode(open_api_params)

urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")

dailyBoxOffice_list = bs.select("dailyBoxOfficeList > dailyBoxOffice")

for dailyBoxOffice in dailyBoxOffice_list:
    print(dailyBoxOffice.select_one("rank").get_text(), end=" ")
    print(dailyBoxOffice.select_one("movieNm").get_text())



