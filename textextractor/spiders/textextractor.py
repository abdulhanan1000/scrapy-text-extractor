import scrapy
import json

class GoogleSearchSpider(scrapy.Spider):
    name = 'text_extractor'

    def start_requests(self):
        url = '' #ENTER URL HERE
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
        }
        yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        # Modify the css selectors to match the tags you want to extract
        headings = response.css('h3::text').getall()
        urls = response.css('a::attr(href)').getall()
        spans = response.css('span::text').getall()

        data = {
            "headings": headings,
            "urls": urls,
            "spans": spans
        }
        
        with open('output.json', 'w') as f:
            json.dump(data, f, indent=4)

