import scrapy


class MovieItem(scrapy.Item):
    num = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    color = scrapy.Field()
    size = scrapy.Field()
    sku = scrapy.Field()
    details = scrapy.Field()
    img_urls = scrapy.Field()
