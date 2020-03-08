# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FilmingLocationsSpiderSpider(CrawlSpider):
    name = 'filming_locations_spider'
    allowed_domains = ['https://onlocationvacations.com/category/daily-filming-locations/']
    start_urls = ['https://onlocationvacations.com/category/daily-filming-locations//']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse(self, response):
		for item in response.xpath('//div[@class="td_module_1 td_module_wrap td-animation-stack td_module_no_thumb td-meta-info-hide"]'):
			yield {
				'title_link' : item.xpath('.//h3[@class="entry-title td-module-title"]/a/@href').extract_first(),
			}
			
		
		next_page_url = response.xpath('//div[@class="page-nav td-pb-padding-side"]/a[last()]/@href').extract_first()
		print(next_page_url)
		if next_page_url is not None:
			yield response.follow(next_page_url, self.parse)

