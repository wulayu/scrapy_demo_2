import scrapy
import json
from scrapy import Request
from demo.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = 'deep_pachong'
    # allowed_domains = ['www.zappos.com']
    start_urls = [f'https://prod.olympus.zappos.com/Search/zso/men-sneakers-athletic-shoes/CK_XARC81wHAAQLiAgMBAhg.zso?limit=100&includes=%5B%22productSeoUrl%22%2C%22pageCount%22%2C%22reviewCount%22%2C%22productRating%22%2C%22onSale%22%2C%22isNew%22%2C%22zsoUrls%22%2C%22isCouture%22%2C%22msaImageId%22%2C%22facetPrediction%22%2C%22phraseContext%22%2C%22currentPage%22%2C%22facets%22%2C%22melodySearch%22%2C%22styleColor%22%2C%22seoBlacklist%22%2C%22seoOptimizedData%22%2C%22enableCrossSiteSearches%22%2C%22termLanderAutoFacetOverride%22%2C%22boostQueryOverride%22%2C%22enableSwatches%22%2C%22onHand%22%2C%22enableBestForYouSort%22%2C%22applySyntheticTwins%22%2C%22imageMap%22%2C%22enableUniversalShoeSizeFacets%22%2C%22enableExplicitSizeFilterPreference%22%2C%22enableSingleShoes%22%2C%22enableMsftAds%22%2C%22enableCrossSiteSearches%22%5D&relativeUrls=true&siteId=1&subsiteId=17&page=0']
    page = 0
    print('正在爬取第1页的信息......')
    url = f'https://prod.olympus.zappos.com/Search/zso/men-sneakers-athletic-shoes/CK_XARC81wHAAQLiAgMBAhg.zso?limit=100&includes=%5B%22productSeoUrl%22%2C%22pageCount%22%2C%22reviewCount%22%2C%22productRating%22%2C%22onSale%22%2C%22isNew%22%2C%22zsoUrls%22%2C%22isCouture%22%2C%22msaImageId%22%2C%22facetPrediction%22%2C%22phraseContext%22%2C%22currentPage%22%2C%22facets%22%2C%22melodySearch%22%2C%22styleColor%22%2C%22seoBlacklist%22%2C%22seoOptimizedData%22%2C%22enableCrossSiteSearches%22%2C%22termLanderAutoFacetOverride%22%2C%22boostQueryOverride%22%2C%22enableSwatches%22%2C%22onHand%22%2C%22enableBestForYouSort%22%2C%22applySyntheticTwins%22%2C%22imageMap%22%2C%22enableUniversalShoeSizeFacets%22%2C%22enableExplicitSizeFilterPreference%22%2C%22enableSingleShoes%22%2C%22enableMsftAds%22%2C%22enableCrossSiteSearches%22%5D&relativeUrls=true&siteId=1&subsiteId=17&page='

    def parse(self, response, **kwargs):
        results = json.loads(response.text)
        for i in range(0, 100):
            item = MovieItem()
            item['num'] = i
            item['title'] = results['results'][i]['brandName']
            item['price'] = results['results'][i]['price']
            item['color'] = results['results'][i]['color']
            item['sku'] = results['results'][i]['productId']
            product_id = item['sku']
            item['details'] = results['results'][i]['productName']
            item['priority'] = 1000 - i
            url = f'https://api.cloudcatalog.zappos.com/v3/productBundle?autolink=brandProductName&entireProduct=true&includeBrand=true&includeImages=true&includeOos=false&includeOosSizing=false&includeSizing=true&includeTsdImages=false&includes=preferredSubsite%2ChardLaunchDate%2CtaxonomyAttributes%2Cdrop%2CfinalSale&productId={product_id}&siteId=1&subsiteId=17'
            yield Request(url, meta={'item': item}, callback=self.parse_details, priority=item['priority'])

        if self.page < 10:
            self.page += 1
            print('正在爬取第%d页的信息......' % (self.page + 1))
            yield scrapy.Request(self.url + str(self.page), callback=self.parse)

    def parse_details(self, response):
        item = response.meta['item']
        results_details = json.loads(response.text)
        item['size'] = results_details['product'][0]['sizeFit']['text']
        item['img_urls'] = results_details['product'][0]['defaultImageUrl']
        yield item
