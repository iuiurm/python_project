# spiders folder안에 rt_spider.py 파일 생성
import scrapy
from rt_crawler.items import RTItem


class RTSpider(scrapy.Spider):
    # Spider 식별자
    name = "My_First_RottenTomatoes"
    allowed_domains = ["rottentomatoes.com"]
    start_urls = [
        "https://www.rottentomatoes.com/top/bestofrt/?year=2018"
    ]

    def parse(self, response):
        for tr in response.xpath('//*[@id="top_movies_main"]/div/table/tr'):
            href = tr.xpath('./td[3]/a/@href').extract()[0]
            url = response.urljoin(href)
            year = response.xpath('//*[@id="top_movies_main"]/div/div[2]/button/text()').extract()[1].strip()
            yield scrapy.Request(url, callback=self.parse_detail_page, meta={"year": year})

    def parse_detail_page(self, response):
        item = RTItem()
        item["year"] = response.meta["year"]
        item["title"] = response.xpath('//*[@id="topSection"]/div[2]/div[1]/h1/text()').extract()[0]
        # item["score"] = response.xpath('//*[@id="topSection"]/div[2]/div[1]/section/section/div[2]/h1/a/span[2]/text()')[0].extract().strip()
        item["score"] = response.xpath('//*[@id="topSection"]/div[2]/div[1]/section/text()').extract().strip()
        yield item


