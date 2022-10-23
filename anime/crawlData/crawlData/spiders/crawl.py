import scrapy
from ..items import CrawlDataItem


# Crawl data:
# Step 1: open terminal
# Step 2: enter: cd crawlData
# Step 3: enter: scrapy crawl manga

class CrawlSpider(scrapy.Spider):
    name = 'manga'
    page_number = 2
    start_urls = [
        # TODO: Change this to your own url
        'https://www.nettruyenme.com/tim-truyen/fantasy-105?page=1'
    ]

    def parse(self, response):
        items = CrawlDataItem()
        all_div_quotes = response.css('div.ModuleContent div.items')

        for quotes in all_div_quotes:
            title = quotes.css("a.jtip::text").extract()
            read = quotes.css("span.pull-left::text").extract()
            comment = quotes.css("span.pull-left::text").extract()
            heart = quotes.css("span.pull-left::text").extract()
            new_chap = quotes.css(".chapter:nth-child(1) a::text").extract()
            time_new_chap = quotes.css("li:nth-child(1) i.time::text").extract()
            url = quotes.css("a.jtip::attr(href)").extract()

            items['title'] = title
            items['read'] = read[1::4]
            items['comment'] = comment[2::4]
            items['heart'] = heart[3::4]
            items['new_chap'] = new_chap
            items['time_new_chap'] = time_new_chap
            items['url'] = url
            yield items

        # TODO: Change this to your own url
        next_page = 'https://www.nettruyenme.com/tim-truyen/fantasy-105?page=' + str(CrawlSpider.page_number) + ''

        # TODO: Change this to your own page number
        if CrawlSpider.page_number <= 94:
            CrawlSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
