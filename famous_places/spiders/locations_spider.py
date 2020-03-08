# -*- coding: utf-8 -*-
import scrapy
import json

url_link = []

with open('famous_locations.json') as json_file:
	data = json.load(json_file)
	for link in data:
		url_link = url_link + [link['title_link']]


class LocationsSpiderSpider(scrapy.Spider):
    name = 'locations_spider'
    # allowed_domains = ['https://onlocationvacations.com/category/daily-filming-locations/']

    def start_requests(self):
        urls = url_link[:]

        for url in urls:
        	yield scrapy.Request(url, self.parse)

    def parse(self, response):
    	for loc in response.xpath('//div[@class="td-post-content"]'):
    		yield {
    			'filming_location' : response.xpath('.//h2/text()').extract_first(),
    			'movie_title' : response.xpath('.//h2/following-sibling::p/em/strong/text()|//h2/following-sibling::p/em/strong/text()').extract_first(),
    			'location' : response.xpath('.//h2/following-sibling::p/strong/text()').extract_first()
    		}