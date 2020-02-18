# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = [
        'https://www.amazon.com/b/ref=bhp_brws_awrd?ie=UTF8&node=6960520011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-leftnav&pf_rd_r=W8FTCESDQAF0FAT79776&pf_rd_r=W8FTCESDQAF0FAT79776&pf_rd_t=101&pf_rd_p=ce27b0b7-e06f-42e8-97c3-c33c4ace221f&pf_rd_p=ce27b0b7-e06f-42e8-97c3-c33c4ace221f&pf_rd_i=283155'
    ]

    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css('.s-access-title::text').extract()
        #product_author = response.css('.a-color-secondary+ .a-color-secondary ,#result 0 .a-color-secondary .a-text-normal').css('::text').get()
        product_author = response.css('.a-color-secondary:nth-child(2) .a-text-normal').css('::text').extract()
        #product_price = response.css('.a-spacing-none:nth-child(2) .sx-price-fractional , .a-spacing-none:nth-child(2) .sx-price-whole').css('::text').get()
        product_price = response.css('.a-spacing-none:nth-child(2) .a-price-whole , .a-spacing-none:nth-child(2) .a-price-fraction').css('::text').extract()
        #product_imagelink = response.css('.cfMarker::attr(src)').extract()
        product_imagelink = response.css('.cfMarker::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items
