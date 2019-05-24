# items.py
# Webpage에서 원하는 부분을 scraping하여 저장할 때
# 사용하는 user define 자료구조 class
import scrapy


# 영화정보에 대한 class 정의
class RTItem(scrapy.Item):
    year = scrapy.Field()
    title = scrapy.Field()
    score = scrapy.Field()

