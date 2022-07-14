import scrapy
import json
from scrapy import Request
from demo.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = 'pachong'
    allowed_domains = ['www.zappos.com']

    def start_requests(self):
        for page in range(10):
            print('正在爬取第%d页的信息......' % page)
            yield Request(
                url=f'https://prod.olympus.zappos.com/Search/zso/men-sneakers-athletic-shoes/'
                    f'CK_XARC81wHAAQLiAgMBAhg.zso?limit=100&includes=%5B%22productSeoUrl%22%2C'
                    f'%22pageCount%22%2C%22reviewCount%22%2C%22productRating%22%2C%22onSale%22%'
                    f'2C%22isNew%22%2C%22zsoUrls%22%2C%22isCouture%22%2C%22msaImageId%22%2C%22fa'
                    f'cetPrediction%22%2C%22phraseContext%22%2C%22currentPage%22%2C%22facets%22%2C'
                    f'%22melodySearch%22%2C%22styleColor%22%2C%22seoBlacklist%22%2C%22seoOptimized'
                    f'Data%22%2C%22enableCrossSiteSearches%22%2C%22termLanderAutoFacetOverride%22%'
                    f'2C%22boostQueryOverride%22%2C%22enableSwatches%22%2C%22onHand%22%2C%22enable'
                    f'BestForYouSort%22%2C%22applySyntheticTwins%22%2C%22imageMap%22%2C%22enableUn'
                    f'iversalShoeSizeFacets%22%2C%22enableExplicitSizeFilterPreference%22%2C%22enab'
                    f'leSingleShoes%22%2C%22enableMsftAds%22%2C%22enableCrossSiteSearches%22%5D&rel'
                    f'ativeUrls=true&siteId=1&subsiteId=17&page={page}')

    def parse(self, response, **kwargs):
        a = json.loads(response.text)
        for i in range(0, 100):
            item = MovieItem()
            item['num'] = i
            item['title'] = a['results'][i]['brandName']
            item['price'] = a['results'][i]['price']
            item['color'] = a['results'][i]['color']
            item['size'] = 'unknown'
            item['sku'] = a['results'][i]['productId']
            item['details'] = a['results'][i]['productName']
            item['img_urls'] = a['results'][i]['productUrl']
            yield item
