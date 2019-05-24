# 08.beautifulSoup_naver_finance.py

# Naver 금융 web page에서 오늘의 환율정보 retrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW"

urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")

span_list = bs.select("#content > div.spot > div.today > p.no_today > em > em > span")
result = []

for span in span_list:
    result.append(span.text)

print("오늘의 원달러환율 : {}원".format("".join(result)))

